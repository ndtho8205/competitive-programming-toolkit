import sys
from importlib import machinery, util
from pathlib import Path

from cptool.utils import errors, rand


class TestgenCommand:
    """Generate a number of test cases using your testgen/generator.py implementation."""

    def __call__(self, args):
        self.handle(args.n)

    def register_arguments(self, parser):
        parser.add_argument(
            "n", metavar="<n>", type=int, help="number of test cases to generated"
        )

    def handle(n: int):
        generator = self._load_testgen_code(testgen_code_path)

        output_dir.mkdir(parents=True, exist_ok=True)

        format_name = f"0{len(str(n))}"
        print(f"Generating test cases in `{output_dir}`")
        for i in range(0, n):
            # TODO: ask before overwrite test cases
            # TODO: fix stack trace when test_generator raises exception
            try:
                sys.stdout = open(output_dir / f"{i:{format_name}}.in", "w")
                test_generator.generate(rand.random)
            except NotImplementedError:
                raise errors.TestgenNotImplemented(testgen_code_path)
            finally:
                sys.stdout.close()
                sys.stdout = sys.__stdout__

        print(f"Successfully generated {n} test cases")

    def _load_testgen_code(self, testgen_code_path: Path):
        if not (testgen_code_path.exists() and testgen_code_path.is_file()):
            raise errors.FileNotFound(testgen_code_path)

        loader = machinery.SourceFileLoader("testgen", str(testgen_code_path))
        spec = util.spec_from_loader(loader.name, loader)
        mod = util.module_from_spec(spec)
        loader.exec_module(mod)
        return mod
