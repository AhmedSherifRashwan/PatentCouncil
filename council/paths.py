"""Where a matter's files live, and how a playbook input spec resolves to them."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

HOME = Path.home()
COUNCIL = HOME / "PatentCouncil"
MATTERS = COUNCIL / "matters"
PROMPTS = HOME / "IP-Filing-Ecosystem" / "prompts"
LESSONS = COUNCIL / "lessons.md"
TOOLS = COUNCIL / "tools"


def newest(directory: Path, stem: str) -> Path:
    """`stem.md`, or the highest `stem.vN.md` beside it."""
    best, best_n = directory / f"{stem}.md", 1
    for p in directory.glob(f"{stem}.v*.md"):
        m = re.fullmatch(rf"{re.escape(stem)}\.v(\d+)\.md", p.name)
        if m and int(m.group(1)) > best_n:
            best, best_n = p, int(m.group(1))
    return best


def next_version(directory: Path, stem: str) -> Path:
    cur = newest(directory, stem)
    m = re.search(r"\.v(\d+)\.md$", cur.name)
    return directory / f"{stem}.v{(int(m.group(1)) if m else 1) + 1}.md"


@dataclass
class Run:
    slug: str
    run: str = "r1"

    @property
    def m(self) -> Path:
        return MATTERS / self.slug

    @property
    def r(self) -> Path:
        return self.m / "runs" / self.run

    @property
    def intake(self) -> Path:
        return self.m / "intake"

    def rel(self, path: Path) -> str:
        try:
            return str(path.relative_to(self.r))
        except ValueError:
            return str(path)

    def description(self) -> Path:
        return newest(self.r, "description")

    def claims(self) -> Path:
        return newest(self.r, "claims")

    def resolve(self, spec: str) -> tuple[list[Path], list[Path]]:
        """A prompt's input spec -> (files to embed, files or folders given by path only)."""
        R, I = self.r, self.intake
        if spec == "intake:disclosure":
            return [I / "disclosure.md"], []
        if spec == "intake:gate-1-answers":
            return [I / "answers.md"], []
        if spec in ("intake:data/*", "intake:drawings", "intake:priority/*"):
            folder = I / spec.split(":")[1].split("/")[0]
            files = sorted(p for p in folder.glob("*") if p.is_file() and p.suffix in (".md", ".txt", ".csv", ".json"))
            return files, [folder]  # text files embedded (size permitting); the folder named for anything else
        if spec == "intake:prior-art/*":
            return [R / "prior-art" / "INDEX.md"], [R / "prior-art" / "refs", I / "prior-art"]
        if spec == "terminology":
            return [R / "terminology" / "LOCKED.md"], []
        if spec == "confirmed_embodiments":
            return [R / "CONFIRMED.md"], []
        if spec == "registry":
            return [R / "registry.json"], []
        if spec == "out:P4/description":
            return [self.description()], []
        if spec == "out:P5/claims":
            return [self.claims()], []
        if spec.startswith("out:"):
            phase, pid = spec[4:].split("/")
            return [R / phase / f"{pid}.md"], []
        if spec in ("package:description", "package:claims"):
            final = R / "package" / f"{spec.split(':')[1]}.md"
            if final.exists():
                return [final], []
            return [self.description() if spec.endswith("description") else self.claims()], []
        if spec == "package:all":
            return [], []  # the task embeds the package explicitly
        return [], []  # findings / corrections / requests: the task embeds exactly what it routes
