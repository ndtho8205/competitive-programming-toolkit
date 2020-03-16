# from cptool.controllers import new


class NewCommand:
    """Create a new problem."""

    def __call__(self, args):
        # new(args.path)
        pass

    def register_arguments(self, parser):
        parser.add_argument("path", metavar="<path>", type=str)
        # parser.set_defaults(func=new)
