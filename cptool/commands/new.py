from pathlib import Path

from cptool.commands import BaseCommand
from cptool.templates import Template
from cptool.utils import errors


class NewCommand(BaseCommand):
    """Create a new problem."""

    def __call__(self, args):
        self.handle(args.path, interactive=True)

    def register_arguments(self, parser):
        parser.add_argument(
            "path", metavar="<path>", type=str, help="problem name or a specified path",
        )

    def handle(self, path: str, interactive: bool):
        problem_dir = Path.cwd() / Path(path)
        problem_name = problem_dir.name

        if problem_dir.exists() and problem_dir.is_dir():
            raise errors.CptoolError(
                "destination `{}` already exists.".format(problem_dir)
            )

        creator = Template(interactive)
        creator.create(problem_dir)

        print(
            "Successfully created problem `{}` in `{}`".format(
                problem_name, problem_dir
            )
        )
