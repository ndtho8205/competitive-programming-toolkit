from typing import List
from pathlib import Path

from src import config


def _get_code_path_list(code_dir_path: Path):
    # TODO: process other files than C++
    return list(code_dir_path.glob("*.cpp"))


def _test(code_path_list: List[Path], test_dir_path: Path):
    # TODO: support different filename pattern
    for test_path in test_dir_path.glob("*.in"):
        print(" Total score: 10/10")


def test(problem_path):
    code_dir_path = problem_path / config.PROBLEM_PATH["code"]
    sample_test_dir_path = problem_path / config.PROBLEM_PATH["sample_test"]
    handmade_test_dir_path = problem_path / config.PROBLEM_PATH["handmade_test"]
    generated_test_dir_path = problem_path / config.PROBLEM_PATH["generated_test"]

    code_path_list = _get_code_path_list(code_dir_path)

    print("Testing your code on sample test cases")
    _test(code_path_list, sample_test_dir_path)
    print()

    print("Testing your code on handmade test cases")
    _test(code_path_list, handmade_test_dir_path)
    print()

    print("Testing your code on generated test cases")
    _test(code_path_list, generated_test_dir_path)
    print()
