import os
from pathlib import Path

CURRENT_PATH = Path(".")
SCRIPT_PATH = Path(os.path.dirname(os.path.realpath(__file__))).parent
TEMPLATE_PATH = SCRIPT_PATH / "template"

PROBLEM_PATH = {
    "code": "code",
    "testgen": "testgen/generator.py",
    "sample_test": "test/sample",
    "handmade_test": "test/handmade",
    "generated_test": "test/generated",
    "temp": "temp",
}