from pathlib import Path

from cptool.templates import template
from cptool.utils import errors


class NewCommand:
    """Create a new problem."""

    def __call__(self, args):
        self.handle(args.path)

    def register_arguments(self, parser):
        parser.add_argument(
            "path", metavar="<path>", type=str, help="problem name or a specified path",
        )

    def handle(self, path: str, interactive: bool = True):
        problem_dir = Path.cwd() / Path(path)
        problem_name = problem_dir.name

        if problem_dir.exists() and problem_dir.is_dir():
            raise errors.CptoolError(
                "destination `{}` already exists.".format(problem_dir)
            )

        template.create(problem_dir, interactive)

        print(
            "Successfully created problem `{}` in `{}`".format(
                problem_name, problem_dir
            )
        )
