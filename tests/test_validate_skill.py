from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "validate_skill.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_skill", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("unable to load validator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ValidateSkillTests(unittest.TestCase):
    def test_repository_contract_is_valid(self):
        validator = load_validator()
        self.assertEqual([], validator.validate())


if __name__ == "__main__":
    unittest.main()
