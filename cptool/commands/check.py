from pathlib import Path

from cptool import Cptool
from cptool.commands import BaseCommand
from cptool.yaml import ProblemYamlValidator


class CheckCommand(BaseCommand):
    """Check the validity of the `project.toml` file."""

    def __call__(self, args):
        self.handle()

    def register_arguments(self, parser):
        pass

    def handle(self):
        problem_yaml_file = Cptool.locale_problem_yaml(Path.cwd())

        validator = ProblemYamlValidator()
        validator.validate(problem_yaml_file)

        print("`problem.yaml` is valid!")
