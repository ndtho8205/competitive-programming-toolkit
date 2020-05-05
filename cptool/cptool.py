from pathlib import Path

from cptool.utils.errors import CptoolError
from cptool.yaml.problem_yaml import ProblemYaml


class Cptool:
    def __init__(self, path: Path):
        problem_yaml_file = self.locale_problem_yaml(path)
        self._problem_yaml = ProblemYaml(problem_yaml_file)
        self._problem_dir = problem_yaml_file.parent

    def locale_problem_yaml(self, path: Path) -> Path:
        candidates = [path]
        candidates.extend(path.parents)
        for path in candidates:
            problem_yaml_file = path / "problem.yaml"
            if problem_yaml_file.exists():
                return problem_yaml_file
        else:
            raise CptoolError(
                "could not find a problem.yaml file in {path} or its parents"
            )

    def codes_dir(self):
        return self._problem_dir / "codes"

    def generated_test_cases_dir(self):
        return self._problem_dir / "test_cases" / "generated"

    def handmade_test_cases_dir(self):
        return self._problem_dir / "test_cases" / "handmade"

    def examples_test_cases_dir(self):
        return self._problem_dir / "test_cases" / "examples"

    def generator_test_cases_file(self):
        return self._problem_dir / "test_cases" / "generator.py"
