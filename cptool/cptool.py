from pathlib import Path

from cptool.utils.errors import CptoolError
from cptool.yaml.problem_yaml import ProblemYaml


class Cptool:
    def __init__(self, problem_yaml_file: Path):
        self._problem_yaml = ProblemYaml(problem_yaml_file)
        self._problem_dir = problem_yaml_file.parent

    @staticmethod
    def locale_problem_yaml(path: Path) -> Path:
        candidates = [path]
        candidates.extend(path.parents)
        for p in candidates:
            problem_yaml_file = p / "problem.yaml"
            if problem_yaml_file.exists():
                return problem_yaml_file
        else:
            raise CptoolError(
                f"could not find a `problem.yaml` file in `{path}` or its parents"
            )

    @property
    def codes_dir(self):
        return self._problem_dir / "codes"

    @property
    def generated_test_cases_dir(self):
        return self._problem_dir / "test_cases" / "generated"

    @property
    def handmade_test_cases_dir(self):
        return self._problem_dir / "test_cases" / "handmade"

    @property
    def examples_test_cases_dir(self):
        return self._problem_dir / "test_cases" / "examples"

    @property
    def test_cases_generator_file(self):
        return self._problem_dir / "test_cases" / "generator.py"
