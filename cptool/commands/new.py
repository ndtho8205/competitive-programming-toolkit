from cptool.controllers import new


class NewCommand:
    """Create a new problem."""

    def __call__(self, env, args):
        new(env.current_dir, args.path, env.template_dir)

    def register_arguments(self, parser):
        parser.add_argument(
            "path", metavar="<path>", type=str, help="problem name or a specified path",
        )
