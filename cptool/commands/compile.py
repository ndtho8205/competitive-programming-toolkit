from cptool.helpers import errors


class CompileCommand:
    """Compile your codes."""

    def __call__(self, env, args):
        raise errors.CommandNotImplemented("compile")

    def register_arguments(self, parser):
        parser.add_argument("path", metavar="<path>", type=str)
