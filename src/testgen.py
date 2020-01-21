import sys
import importlib.machinery
from pathlib import Path

from src import utils, config


def generate(problem_dir: Path, n_test_case: int):
    generator_path = problem_dir / config.PROBLEM_PATH["testgen"]
    output_dir = problem_dir / config.PROBLEM_PATH["generated_test"]

    if not (generator_path.exists() and generator_path.is_file()):
        raise FileNotFoundError(f"{generator_path} does not exists.")

    loader = importlib.machinery.SourceFileLoader("testgen", str(generator_path))
    test_generator = loader.load_module("testgen")

    format_name = f"0{len(str(n_test_case))}"
    print(f"Generating test cases in {output_dir}")
    for i in range(0, n_test_case):
        # TODO: ask before overwrite test cases
        sys.stdout = open(output_dir / f"{i:{format_name}}.in", "w")
        test_generator.generate(utils.random)
        sys.stdout.close()

    sys.stdout = sys.__stdout__
    print(f"Successfully generated {n_test_case} test cases")
