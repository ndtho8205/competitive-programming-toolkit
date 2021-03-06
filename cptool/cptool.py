import os
from pathlib import Path

from cptool.utils.errors import CptoolError
from cptool.yaml.problem_yaml import ProblemYaml


class Cptool:
    def __init__(self, problem_yaml_file: Path):
        self._problem_yaml = ProblemYaml(problem_yaml_file)
        self._problem_dir = problem_yaml_file.parent
        os.chdir(self._problem_dir)

    @staticmethod
    def locale_problem_yaml(path: Path) -> Path:
        candidates = [path]
        candidates.extend(path.parents)
        print(candidates)
        for p in candidates:
            problem_yaml_file = p / "problem.yaml"
            if problem_yaml_file.exists():
                return problem_yaml_file
        else:
            raise CptoolError(
                f"could not find a `problem.yaml` file in `{path}` or its parents"
            )

    @property
    def problem_dir(self):
        return self._problem_dir

    @property
    def codes_dir(self):
        return Path("codes")

    @property
    def generated_test_cases_dir(self):
        return Path("test_cases") / "generated"

    @property
    def handmade_test_cases_dir(self):
        return Path("test_cases") / "handmade"

    @property
    def examples_test_cases_dir(self):
        return Path("test_cases") / "examples"

    @property
    def test_cases_generator_file(self):
        return Path("test_cases") / "generator.py"

    @property
    def compiled_codes_dir(self):
        return Path("target") / "compiled_codes"

    @property
    def target_generated_test_cases_dir(self):
        return Path("target") / "generated"

    @property
    def target_handmade_test_cases_dir(self):
        return Path("target") / "handmade"

    @property
    def target_examples_test_cases_dir(self):
        return Path("target") / "examples"
