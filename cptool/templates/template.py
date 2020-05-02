from pathlib import Path

from cptool.templates.problem_yaml_generator import ProblemYamlGenerator

TEST_CASE_GENERATOR_DEFAULT = u"""\
from typing import Callable

# MIN_N = 1
# MAX_N = 1000000


def generate(f_rand: Callable[[int, int], int]):
    # f_rand(min_range, max_range) is a function
    # that return a pesudo-random integer
    # in [min_range, max_range]
    # print(f_rand(MIN_N, MAX_N))
    raise NotImplementedError()


if __name__ == "__main__":
    generate(f_rand=lambda x, y: 3)
"""


def create(problem_dir: Path, interactive=True):
    problem_dir.mkdir(parents=True, exist_ok=True)

    _create_structure(problem_dir)
    _create_problem_yaml(problem_dir, interactive)
    _create_readme(problem_dir)


def _create_structure(path: Path):
    code_dir = path / "codes"
    code_dir.mkdir()

    test_cases = ["generated", "handmade", "examples"]
    test_cases_dir = path / "test_cases"
    test_cases_dir.mkdir()
    for test in test_cases:
        (test_cases_dir / test).mkdir()

    test_case_generator_file = test_cases_dir / "generator.py"
    with test_case_generator_file.open("w", encoding="utf-8") as f:
        f.write(TEST_CASE_GENERATOR_DEFAULT)


def _create_problem_yaml(path: Path, interactive: bool = True):
    problem_yaml = ProblemYamlGenerator(path.name).generate(interactive)
    problem_yaml.export(path / "problem.yaml")


def _create_readme(path: Path):
    readme_file = path / "README.md"
    readme_file.touch()
