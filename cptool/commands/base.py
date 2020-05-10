from pathlib import Path

from cptool.cptool import Cptool


class BaseCommand:
    def __init__(self):
        self._cptool = None

    @property
    def cptool(self):
        if not self._cptool:
            problem_yaml_file = Cptool.locale_problem_yaml(Path.cwd())
            self._cptool = Cptool(problem_yaml_file)

        return self._cptool

    def __call__(self, args):
        raise NotImplementedError()

    def register_arguments(self, parser):
        raise NotImplementedError()
