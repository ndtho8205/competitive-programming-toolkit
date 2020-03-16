from cptool.controllers import testgen


class TestgenCommand:
    """Generate a number of test cases using your testgen/generator.py implementation."""

    def __call__(self, env, args):
        testgen(args.n, env.testgen_code_path, env.generated_test_dir)

    def register_arguments(self, parser):
        parser.add_argument("n", metavar="<number of test cases>", type=int)
