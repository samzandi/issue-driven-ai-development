# Contributing

Issue-Driven AI Development welcomes focused contributions that improve context discipline, work-item quality, verification, or GitHub integration.

## Before opening a pull request

- Open or reference an issue for non-trivial work.
- Keep the change narrowly scoped.
- Add or update validation where behavior changes.
- Run `python tools/validate_skill.py`.
- Run `python -m unittest discover -s tests -p 'test_*.py'`.
- Update documentation when the workflow contract changes.
- Never commit credentials, private project records, customer data, or secrets.

## Pull-request expectations

Explain the user problem, intended behavior, non-goals, verification performed, security/privacy implications, and known limitations. A change is complete only when the claimed behavior is backed by evidence.
