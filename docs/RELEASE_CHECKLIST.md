# Release Checklist

Before publishing a versioned release:

- [ ] `python tools/validate_skill.py` passes.
- [ ] Unit tests pass on supported Python versions.
- [ ] `SKILL.md` metadata and workflow rules match the documented behavior.
- [ ] Referenced files and GitHub mapping documentation exist.
- [ ] Security and privacy boundaries are reviewed.
- [ ] No secrets or private project records are committed.
- [ ] Release notes list behavior changes and known limitations.
- [ ] The exact release commit is recorded.

A green structural check does not prove that every external agent runtime behaves identically. Runtime-specific claims require runtime-specific evidence.
