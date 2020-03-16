from cptool.helpers import errors


class DiffCommand:
    """Check if there is any differences among input files (not implemented)."""

    def __call__(self, env, args):
        raise errors.CommandNotImplemented("diff")

    def register_arguments(self, parser):
        parser.add_argument("files", metavar="<file>", type=str, nargs="+")
