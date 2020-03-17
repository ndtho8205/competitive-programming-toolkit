from cptool.controllers import test


class TestCommand:
    """Test your codes on test cases."""

    def __call__(self, env, args):
        print(args)
        if args.kind == "all":
            test.test_all(env)
        elif args.kind == "sample":
            test.test_sample(env)
        elif args.kind == "handmade":
            test.test_handmade(env)
        elif args.kind == "generated":
            test.test_generated(env)

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
