#!/usr/bin/env python3
"""Regenerate the README resource library from data/resources.json."""
from __future__ import annotations

import json
import re
from collections import Counter, OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
DATA = ROOT / "data" / "resources.json"
START = "<!-- RESOURCE_LIBRARY_START -->"
END = "<!-- RESOURCE_LIBRARY_END -->"

CATEGORY_ICONS = {'Programming & Tools': '🧰', 'Numerical Methods': '🔢', 'Mathematics': '📐', 'Physics & Mechanics': '⚙️', 'CFD & Fluid Mechanics': '🌊', 'FEA & Solid Mechanics': '🏗️', 'HPC & Parallel Computing': '🚀', 'Data, ML & Scientific AI': '🧠', 'Optimization & Control': '🎯', 'Research Workflow': '🔬'}
CATEGORY_DESCRIPTIONS = {'Programming & Tools': 'Scientific programming, Git, Linux, debugging, and reproducible developer workflows.', 'Numerical Methods': 'Algorithms for equations, ODEs, PDEs, integration, interpolation, and error analysis.', 'Mathematics': 'Calculus, linear algebra, differential equations, probability, and mathematical foundations.', 'Physics & Mechanics': 'Fluid dynamics, thermodynamics, statics, dynamics, and continuum mechanics.', 'CFD & Fluid Mechanics': 'Finite-volume methods, solvers, meshing, turbulence modeling, and verification.', 'FEA & Solid Mechanics': 'Finite-element theory, structural simulation, open-source frameworks, and examples.', 'HPC & Parallel Computing': 'MPI, OpenMP, GPU programming, performance engineering, and scalable solvers.', 'Data, ML & Scientific AI': 'Scientific Python, machine learning, PINNs, operator learning, and reduced-order models.', 'Optimization & Control': 'Design optimization, adjoints, convex methods, system dynamics, and control.', 'Research Workflow': 'Reproducibility, technical writing, data management, citation, and collaboration.'}


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

    out: list[str] = []
    for category, items in grouped.items():
        levels = Counter(item["level"] for item in items)
        out.extend([
            f'<a id="{anchor(category)}"></a>',
            '<details>',
            f'<summary><strong>{CATEGORY_ICONS.get(category, "📚")} {esc(category)}</strong> &nbsp;·&nbsp; {len(items)} resources &nbsp;·&nbsp; '
            f'{levels.get("Beginner", 0)} beginner / {levels.get("Intermediate", 0)} intermediate / {levels.get("Advanced", 0)} advanced</summary>',
            '',
            f'> {CATEGORY_DESCRIPTIONS.get(category, "")}',
            '',
            '| Resource | Focus | Level | Format | Access |',
            '|---|---|:---:|:---:|:---:|',
        ])
        for item in items:
            star = ' ⭐' if item.get('featured') else ''
            title = f"**[{esc(item['title'])}]({item['url']})**{star}<br><sub>{esc(item['description'])}</sub>"
            tags = ' · '.join(f"`{esc(tag)}`" for tag in item.get('tags', [])[:4]) or '—'
            access = '✅ Free' if item.get('free') else '◐ Mixed'
            out.append(
                f"| {title} | {tags} | **{esc(item['level'])}** | {esc(item['type'])} | {access} |"
            )
        out.extend(['', '</details>', ''])
    return '\n'.join(out).rstrip()


def main() -> None:
    resources = json.loads(DATA.read_text(encoding='utf-8'))
    current = README.read_text(encoding='utf-8')
    if START not in current or END not in current:
        raise SystemExit(f'Missing README markers: {START} and {END}')
    before, rest = current.split(START, 1)
    _, after = rest.split(END, 1)
    library = build_library(resources)
    README.write_text(f"{before}{START}\n\n{library}\n{END}{after}", encoding='utf-8')
    print(f'Updated README.md with {len(resources)} resources.')


if __name__ == '__main__':
    main()
