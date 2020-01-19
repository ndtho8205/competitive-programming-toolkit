import sys
import importlib.machinery
from pathlib import Path

from . import utils, config


def generate(problem_path: Path, n_test_case: int):
    logic_path = problem_path / config.PROBLEM_PATH["logic"]
    output_path = problem_path / config.PROBLEM_PATH["generated_test"]

    if not (logic_path.exists() and logic_path.is_file()):
        raise FileNotFoundError(f"{logic_path} does not exists.")

    loader = importlib.machinery.SourceFileLoader("logic", str(logic_path))
    logic = loader.load_module("logic")

    format_name = f"0{len(str(n_test_case))}"
    print(f"Generating test cases in {output_path}")
    for i in range(0, n_test_case):
        sys.stdout = open(output_path / f"{i:{format_name}}.in", "w")
        logic.logic(utils.random())
        sys.stdout.close()

    sys.stdout = sys.__stdout__
    print(f"Successfully generated {n_test_case} test cases")
