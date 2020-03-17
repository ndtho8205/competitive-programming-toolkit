from cptool.controllers import test


class TestCommand:
    """Test your codes on test cases."""

    def __call__(self, env, args):
        test(env, args.kind)

    def register_arguments(self, parser):
        parser.add_argument(
            "kind",
            metavar="<kind>",
            type=str,
            nargs="?",
            choices=["all", "sample", "handmade", "generated"],
            default="all",
            help=" ".join(
                [
                    "specified where to test your codes.",
                    "Options: ['all', 'sample', 'handmade', 'generated'].",
                    "Default: 'all'.",
                ]
            ),
        )
