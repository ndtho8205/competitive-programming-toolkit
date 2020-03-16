import os
import sys
from pathlib import Path

PROBLEM_PATH = {
    "code": "code",
    "testgen": "testgen/generator.py",
    "sample_test": "test/sample",
    "handmade_test": "test/handmade",
    "generated_test": "test/generated",
    "target": "target",
}


class Env:
    is_linux = False
    is_windows = False
    current_dir = None

    def __init__(self):
        self.is_linux = sys.platform == "linux"
        self.is_windows = sys.platform == "win32"

        self.cptool_path = Path(os.path.dirname(os.path.realpath(__file__))).parent
        self.current_dir = Path(".")

    @property
    def template_dir(self):
        return self.cptool_path / "template"

    @property
    def code_dir(self):
        return self.current_dir / PROBLEM_PATH["code"]

    @property
    def testgen_code_path(self):
        return self.current_dir / PROBLEM_PATH["testgen"]

    @property
    def sample_test_dir(self):
        return self.current_dir / PROBLEM_PATH["sample_test"]

    @property
    def handmade_test_dir(self):
        return self.current_dir / PROBLEM_PATH["handmade_test"]

    @property
    def generated_test_dir(self):
        return self.current_dir / PROBLEM_PATH["generated_test"]

    @property
    def target_dir(self):
        return self.current_dir / PROBLEM_PATH["target"]
