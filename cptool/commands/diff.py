class DiffCommand:
    """Check if there is any differences among input files (not implemented)."""

    def __call__(self, args):
        raise NotImplementedError("Command `diff` has not been implemented.")

    def register_arguments(self, parser):
        parser.add_argument("files", metavar="<file>", type=str, nargs="+")
