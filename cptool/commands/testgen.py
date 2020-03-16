class TestgenCommand:
    """Generate a number of test cases using your testgen/generator.py implementation."""

    def __call__(self, args):
        print(args)

    def register_arguments(self, parser):
        parser.add_argument("n", metavar="<number of test cases>", type=int)
