from pathlib import Path

from cptool import Cptool


class CheckCommand:
    """Check the validity of the `project.toml` file."""

    def __call__(self, args):
        self.handle()

    def register_arguments(self, parser):
        pass

    def handle(self):
        self._cptool = Cptool(Path.cwd())
        print("`problem.yaml` is valid!")
