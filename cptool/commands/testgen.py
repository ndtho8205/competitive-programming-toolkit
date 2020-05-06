import sys
from importlib import machinery, util
from pathlib import Path

from cptool import Cptool
from cptool.commands import BaseCommand
from cptool.utils import rand
from cptool.utils.errors import CptoolError


class TestgenCommand(BaseCommand):
    """Generate a number of test cases using your testgen/generator.py implementation."""

    def __call__(self, args):
        self.handle(args.n)

    def register_arguments(self, parser):
        parser.add_argument(
            "n", metavar="<n>", type=int, help="number of test cases to generated"
        )

    def handle(self, n: int):
        generator_file = self.cptool.test_cases_generator_file
        generator = self._load_generator(generator_file)

        generated_dir = self.cptool.generated_test_cases_dir
        generated_dir.mkdir(parents=True, exist_ok=True)

        format_name = f"0{len(str(n))}"
        print(f"Generating test cases in `{generated_dir}`")
        for i in range(1, n + 1):
            # TODO: ask before overwrite test cases
            # TODO: fix stack trace when test_generator raises exception
            try:
                sys.stdout = open(generated_dir / f"{i:{format_name}}.in", "w")
                generator.generate(rand.random)
            except NotImplementedError:
                raise CptoolError(
                    "`{}` must be implemented first before generating test cases.".format(
                        generator_file
                    )
                )
            finally:
                sys.stdout.close()
                sys.stdout = sys.__stdout__

        print(f"Successfully generated {n} test cases")

    def _load_generator(self, generator_file: Path):
        if not (generator_file.exists() and generator_file.is_file()):
            raise FileNotFoundError("`{generator_file}` not found.")

        loader = machinery.SourceFileLoader("testgen", str(generator_file))
        spec = util.spec_from_loader(loader.name, loader)
        mod = util.module_from_spec(spec)
        loader.exec_module(mod)
        return mod
