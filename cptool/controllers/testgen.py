import sys
from importlib import machinery, util
from pathlib import Path

from cptool.helpers import rand, errors


def testgen(n: int, testgen_code_path: Path, output_dir: Path):
    test_generator = _load_testgen_code(testgen_code_path)

    output_dir.mkdir(parents=True, exist_ok=True)

    format_name = f"0{len(str(n))}"
    print(f"Generating test cases in `{output_dir}`")
    for i in range(0, n):
        # TODO: ask before overwrite test cases
        try:
            sys.stdout = open(output_dir / f"{i:{format_name}}.in", "w")
            test_generator.generate(rand.random)
        except NotImplementedError:
            raise errors.TestgenNotImplemented(testgen_code_path)
        finally:
            sys.stdout.close()
            sys.stdout = sys.__stdout__

    print(f"Successfully generated {n} test cases")


def _load_testgen_code(testgen_code_path: Path):
    if not (testgen_code_path.exists() and testgen_code_path.is_file()):
        raise errors.FileNotFound(testgen_code_path)

    loader = machinery.SourceFileLoader("testgen", str(testgen_code_path))
    spec = util.spec_from_loader(loader.name, loader)
    mod = util.module_from_spec(spec)
    loader.exec_module(mod)
    return mod
