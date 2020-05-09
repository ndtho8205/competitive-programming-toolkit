from pathlib import Path
from typing import List

from cptool.commands import BaseCommand
from cptool.languages import BaseCodeFile, get_lang
from cptool.utils import diff, errors


class TestCommand(BaseCommand):
    """Test your codes on test cases."""

    def __call__(self, args):
        self.handle(args.kind)

    def register_arguments(self, parser):
        parser.add_argument(
            "kind",
            metavar="<kind>",
            type=str,
            nargs="?",
            choices=["all", "examples", "handmade", "generated"],
            default="all",
            help=" ".join(
                [
                    "specified where to test your codes.",
                    "Options: ['all', 'examples', 'handmade', 'generated'].",
                    "Default: 'all'.",
                ]
            ),
        )

    def handle(self, kind):
        codes = self._compile(self.cptool.codes_dir, self.cptool.compiled_codes_dir)

        print()

        if kind == "all":
            self._test_all(codes)
        if kind == "examples":
            self._test_examples(codes)
        elif kind == "handmade":
            self.test_handmade(codes)
        elif kind == "generated":
            self.test_generated(codes)

    def _test_all(self, codes: List[BaseCodeFile]):
        self._test_examples(codes)
        self._test_handmade(codes)
        self._test_generated(codes)

    def _test_examples(self, codes: List[BaseCodeFile]):
        print("Running your code on examples test cases")

        input_dir = self.cptool.examples_test_cases_dir
        output_dir = self.cptool.target_examples_test_cases_dir

        self._test(codes, input_dir, output_dir)

    def _test_handmade(self, codes: List[BaseCodeFile]):
        print("Running your code on handmade test cases")

        input_dir = self.cptool.handmade_test_cases_dir
        output_dir = self.cptool.target_handmade_test_cases_dir

        self._test(codes, input_dir, output_dir)

    def _test_generated(self, codes: List[BaseCodeFile]):
        print("Running your code on generated test cases")

        input_dir = self.cptool.generated_test_cases_dir
        output_dir = self.cptool.target_generated_test_cases_dir

        self._test(codes, input_dir, output_dir)

    def _compile(self, code_dir: Path, compiled_code_dir: Path):
        codes = list(get_lang(code) for code in code_dir.glob("*") if code.is_file())
        if not codes:
            raise errors.CptoolError("cannot find any code file in `codes` directory.")
        for code in codes:
            code.compile(compiled_code_dir)

        return codes

    def _test(self, codes: List[BaseCodeFile], input_dir: Path, output_dir: Path):
        results = self._get_output(codes, input_dir, output_dir)

        have_diff = False
        for in_name, output_path_list in results.items():
            diff_output = diff.diff(output_path_list)
            if diff_output:
                have_diff = True
                print(f"  ❌ Test case {in_name}: {diff_output}")

        if not have_diff:
            print("  ✅ There are no differences among your codes' outputs :)")

    def _get_output(self, codes: List[BaseCodeFile], input_dir: Path, output_dir: Path):
        # TODO: support different filename pattern
        output_dir.mkdir(parents=True, exist_ok=True)

        total_code = len(codes)
        total_test = len(list(input_dir.glob("*.in")))

        if not total_test:
            print(f"\r\x1b[2K  {total_test} test cases are tested.")

        results = {}
        for input_idx, input_file in enumerate(input_dir.glob("*.in")):
            # with each input file, generate output list by executing all user codes
            output_path_list = []

            # append the solution for input file if exists
            solution_file = input_file.with_suffix(".ok")
            if solution_file.exists() and solution_file.is_file():
                output_path_list.append(solution_file)

            # execute user code and append its result
            for code_idx, code in enumerate(codes):
                self._print_progress(
                    input_idx,
                    input_file.name,
                    total_test,
                    code_idx,
                    code._code_file.name,
                    total_code,
                )

                output_path = (
                    output_dir / f"{input_file.stem}_{code._code_file.stem}.ans"
                )
                code.execute(input_file, output_path)
                output_path_list.append(output_path)

            results[input_file.name] = output_path_list

        return results

    def _print_progress(
        self, test_idx, test_name, total_test, code_idx, code_name, total_code
    ):
        if test_idx + 1 == total_test and code_idx + 1 == total_code:
            print(f"\r\x1b[2K  {total_test} test cases are tested.")
        else:
            print(
                "".join(
                    [
                        f"\r  {test_idx + 1}/{total_test} test cases > ",
                        f"Code {code_idx + 1}/{total_code} >> {code_name} on {test_name}",
                    ]
                ),
                end="",
            )
