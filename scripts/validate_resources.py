#!/usr/bin/env python3
"""Validate the computational engineering resource dataset."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "resources.json"
REQUIRED = {"title", "url", "category", "level", "type", "description", "tags", "featured", "free"}
LEVELS = {"Beginner", "Intermediate", "Advanced"}
TAG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def fail(message: str) -> None:
    print(f"ERROR: {message}")


def main() -> int:
    try:
        resources = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"Unable to read {DATA_FILE}: {exc}")
        return 1

    if not isinstance(resources, list) or not resources:
        fail("Dataset must be a non-empty JSON array.")
        return 1

    errors = 0
    seen_titles: set[str] = set()
    seen_urls: set[str] = set()

    for index, item in enumerate(resources, start=1):
        prefix = f"resource #{index}"
        if not isinstance(item, dict):
            fail(f"{prefix} is not an object")
            errors += 1
            continue

        missing = REQUIRED - item.keys()
        extra = item.keys() - REQUIRED
        if missing:
            fail(f"{prefix} missing fields: {sorted(missing)}")
            errors += 1
        if extra:
            fail(f"{prefix} has unsupported fields: {sorted(extra)}")
            errors += 1

        title = item.get("title")
        url = item.get("url")
        if not isinstance(title, str) or not title.strip():
            fail(f"{prefix} has an invalid title")
            errors += 1
        elif title.casefold() in seen_titles:
            fail(f"duplicate title: {title}")
            errors += 1
        else:
            seen_titles.add(title.casefold())

        if not isinstance(url, str) or urlparse(url).scheme not in {"http", "https"}:
            fail(f"{prefix} has an invalid URL: {url!r}")
            errors += 1
        elif url.rstrip("/").casefold() in seen_urls:
            fail(f"duplicate URL: {url}")
            errors += 1
        else:
            seen_urls.add(url.rstrip("/").casefold())

        if item.get("level") not in LEVELS:
            fail(f"{prefix} has invalid level: {item.get('level')!r}")
            errors += 1

        for field in ("category", "type", "description"):
            if not isinstance(item.get(field), str) or not item[field].strip():
                fail(f"{prefix} has an invalid {field}")
                errors += 1

        tags = item.get("tags")
        if not isinstance(tags, list) or not tags:
            fail(f"{prefix} must contain at least one tag")
            errors += 1
        elif any(not isinstance(tag, str) or not TAG_RE.fullmatch(tag) for tag in tags):
            fail(f"{prefix} has invalid tags; use lowercase kebab-case")
            errors += 1

        if not isinstance(item.get("featured"), bool) or not isinstance(item.get("free"), bool):
            fail(f"{prefix} featured/free fields must be booleans")
            errors += 1

    if errors:
        print(f"Validation failed with {errors} error(s).")
        return 1

    print(f"Validated {len(resources)} resources across {len({r['category'] for r in resources})} categories.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
