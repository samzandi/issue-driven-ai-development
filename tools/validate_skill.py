from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "README.md",
    "SKILL.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "CODE_OF_CONDUCT.md",
    "MAINTAINERS.md",
    "CHANGELOG.md",
    "PROJECT_CONTEXT_INDEX.md",
    "agents/openai.yaml",
    "references/github-mapping.md",
    "references/product-principles.md",
    "references/project-record.md",
    "references/work-item.md",
    "docs/RELEASE_CHECKLIST.md",
    "docs/OPEN_SOURCE_MAINTENANCE.md",
)


def validate() -> list[str]:
    errors: list[str] = []

    for relative in REQUIRED_FILES:
        path = ROOT / relative
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"missing or empty required file: {relative}")

    skill_path = ROOT / "SKILL.md"
    if skill_path.is_file():
        text = skill_path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            errors.append("SKILL.md must start with YAML-style front matter")
        if "\nname: issue-driven-ai-development\n" not in text:
            errors.append("SKILL.md front matter must declare the canonical skill name")
        if "\ndescription:" not in text:
            errors.append("SKILL.md front matter must include a description")
        for required_reference in (
            "references/project-record.md",
            "references/work-item.md",
            "references/github-mapping.md",
        ):
            if required_reference not in text:
                errors.append(f"SKILL.md does not reference {required_reference}")

    readme_path = ROOT / "README.md"
    if readme_path.is_file():
        readme = readme_path.read_text(encoding="utf-8").lower()
        for phrase in ("mit", "contributing", "security", "pre-1.0"):
            if phrase not in readme:
                errors.append(f"README.md must mention {phrase}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validation passed for {len(REQUIRED_FILES)} required files and the skill contract.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
