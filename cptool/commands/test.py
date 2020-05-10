from pathlib import Path
from typing import List

from cptool.commands import BaseCommand
from cptool.languages import BaseCodeFile, get_lang
from cptool.utils import TestCase, errors


class TestCommand(BaseCommand):
    """Test your codes on test cases."""

    def __init__(self):
        super().__init__()

    def __call__(self, args):
        self.handle(args.code_regexp, args.kind)

    def register_arguments(self, parser):
        parser.add_argument(
            "-c",
            "--code-regexp",
            metavar="<regexp>",
            type=str,
            default="*",
            help="pattern to match code filename",
        )
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

    def handle(self, code_regexp: str, kind: str):
        if kind == "all":
            kinds = ["examples", "handmade", "generated"]
        else:
            kinds = [kind]

        print("Preparing code files...")
        code_files = self._prepare_code_files(code_regexp)

        if "examples" in kinds:
            print("Examples test cases:")
            self._test(
                code_files,
                self.cptool.examples_test_cases_dir,
                self.cptool.target_examples_test_cases_dir,
            )
        if "handmade" in kinds:
            print("Handmade test cases:")
            self._test(
                code_files,
                self.cptool.handmade_test_cases_dir,
                self.cptool.target_handmade_test_cases_dir,
            )
        if "generated" in kinds:
            print("Generated test cases:")
            self._test(
                code_files,
                self.cptool.generated_test_cases_dir,
                self.cptool.target_generated_test_cases_dir,
            )

    def _test(
        self, code_files: List[BaseCodeFile], test_cases_dir: Path, answer_dir: Path
    ):
        answer_dir.mkdir(parents=True, exist_ok=True)
        test_cases = self._prepare_test_cases(test_cases_dir,)

        if not test_cases:
            print("  0 test cases found")
            return

        for test_case_idx, test_case in enumerate(test_cases):
            for code_idx, code in enumerate(code_files):
                ans = answer_dir / f"{test_case.inp.stem}_{code.code_file.stem}.ans"
                code.execute(test_case.inp, ans)
                test_case.add_ans(ans)

        have_diff = False
        for test_case in test_cases:
            diff_output = test_case.diff()
            if diff_output:
                have_diff = True
                print(f"  ❌ Test case {test_case.inp}: {diff_output}")

        if not have_diff:
            print("  ✅ There are no differences among your codes' answers :)")

    def _prepare_code_files(self, code_regexp: str):
        code_files = list(
            get_lang(file)
            for file in self.cptool.codes_dir.glob(code_regexp)
            if file.is_file()
        )

        if not code_files:
            raise errors.CptoolError("cannot find any code file in `codes` directory.")

        self.cptool.compiled_codes_dir.mkdir(parents=True, exist_ok=True)

        for code in code_files:
            code.compile(self.cptool.compiled_codes_dir)
            print(f"  {code.code_file}")

        return code_files

    def _prepare_test_cases(self, test_cases_dir: Path):
        test_cases = []
        for inp_file in test_cases_dir.glob("*.in"):
            solution_file = inp_file.with_suffix(".ok")

            test_cases.append(
                TestCase(
                    inp_file,
                    solution_file
                    if (solution_file.exists() and solution_file.is_file())
                    else None,
                )
            )
        return test_cases

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
