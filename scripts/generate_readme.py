#!/usr/bin/env python3
"""Regenerate README.md from data/resources.json.

This script delegates to the repository's checked-in template snapshot. To update
introductory copy, edit README.md and this script together. Resource entries are
always generated from the JSON source of truth.
"""
from __future__ import annotations

import json
import re
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
DATA = ROOT / "data" / "resources.json"

CATEGORY_ICONS = {
    "Programming & Tools": "🧰", "Numerical Methods": "🔢", "Mathematics": "📐",
    "Physics & Mechanics": "⚙️", "CFD & Fluid Mechanics": "🌊",
    "FEA & Solid Mechanics": "🏗️", "HPC & Parallel Computing": "🚀",
    "Data, ML & Scientific AI": "🧠", "Optimization & Control": "🎯",
    "Research Workflow": "🔬",
}

CATEGORY_DESCRIPTIONS = {
    "Programming & Tools": "Scientific programming, version control, Linux, debugging, and developer workflows.",
    "Numerical Methods": "Algorithms for solving equations, ODEs, PDEs, interpolation, integration, and numerical error.",
    "Mathematics": "Calculus, linear algebra, differential equations, probability, and mathematical foundations.",
    "Physics & Mechanics": "Fluid dynamics, thermodynamics, statics, dynamics, and continuum-mechanics foundations.",
    "CFD & Fluid Mechanics": "Finite-volume methods, CFD theory, OpenFOAM, SU2, verification, and turbulence modeling.",
    "FEA & Solid Mechanics": "Finite-element methods, structural mechanics, open-source solvers, and practical tutorials.",
    "HPC & Parallel Computing": "MPI, OpenMP, GPU programming, performance engineering, and scalable scientific computing.",
    "Data, ML & Scientific AI": "Scientific Python, machine learning, differentiable computing, PINNs, and operator learning.",
    "Optimization & Control": "Design optimization, convex methods, multidisciplinary optimization, and dynamical systems.",
    "Research Workflow": "Reproducibility, scientific writing, data management, citation, and collaborative research practice.",
}

START = "<!-- RESOURCE_LIBRARY_START -->"
END = "<!-- RESOURCE_LIBRARY_END -->"


def esc(value: object) -> str:
    return str(value).replace("|", r"\|").replace("\n", " ")


def anchor(text: str) -> str:
    value = text.lower().replace("&", "").replace(",", "")
    value = re.sub(r"[^a-z0-9 ]+", "", value)
    return re.sub(r"\s+", "-", value.strip())


def build_library(resources: list[dict]) -> str:
    grouped: OrderedDict[str, list[dict]] = OrderedDict()
    for item in resources:
        grouped.setdefault(item["category"], []).append(item)

    out = [START, ""]
    for category, items in grouped.items():
        icon = CATEGORY_ICONS.get(category, "📚")
        out += [
            f'<a id="{anchor(category)}"></a>',
            "<details>",
            f"<summary><strong>{icon} {esc(category)}</strong> — {len(items)} resources</summary>",
            "", CATEGORY_DESCRIPTIONS.get(category, ""), "",
            "| Resource | Level | Format | Access | Description |",
            "|---|---|---|---|---|",
        ]
        for item in items:
            access = "✅ Free" if item.get("free") else "◐ Mixed/Paid"
            star = " ⭐" if item.get("featured") else ""
            out.append(
                f"| **[{esc(item['title'])}]({item['url']})**{star} | "
                f"{esc(item['level'])} | {esc(item['type'])} | {access} | "
                f"{esc(item['description'])} |"
            )
        out += ["", "</details>", ""]
    out.append(END)
    return "\n".join(out)


def main() -> None:
    resources = json.loads(DATA.read_text(encoding="utf-8"))
    current = README.read_text(encoding="utf-8")
    if START not in current or END not in current:
        raise SystemExit(f"README markers {START} and {END} were not found.")
    before, tail = current.split(START, 1)
    _, after = tail.split(END, 1)
    README.write_text(before + build_library(resources) + after, encoding="utf-8")
    print(f"Updated {README} with {len(resources)} resources.")


if __name__ == "__main__":
    main()
