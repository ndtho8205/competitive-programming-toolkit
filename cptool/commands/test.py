from pathlib import Path
from typing import List

from cptool.languages import BaseLanguage, get_lang
from cptool.utils import diff, errors


class TestCommand:
    """Test your codes on test cases."""

    def __call__(self, env, args):
        self.handle(env, args.kind)

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

    def handle(env, kind):
        def test(env, kind):
            codes = _compile(env.code_dir, env.target_code_dir)

        print()

        if kind == "all":
            _test_all(codes, env)
        if kind == "sample":
            _test_sample(codes, env)
        elif kind == "handmade":
            _test_handmade(codes, env)
        elif kind == "generated":
            _test_generated(codes, env)

    def _test_all(codes: List[BaseLanguage], env):
        _test_sample(codes, env)
        _test_handmade(codes, env)
        _test_generated(codes, env)

    def _test_sample(codes: List[BaseLanguage], env):
        print("Running your code on sample test cases")

        input_dir = env.sample_test_dir
        output_dir = env.target_sample_test_dir

        _test(codes, input_dir, output_dir)

    def _test_handmade(codes: List[BaseLanguage], env):
        print("Running your code on handmade test cases")

        input_dir = env.handmade_test_dir
        output_dir = env.target_handmade_test_dir

        _test(codes, input_dir, output_dir)

    def _test_generated(codes: List[BaseLanguage], env):
        print("Running your code on generated test cases")

        input_dir = env.generated_test_dir
        output_dir = env.target_generated_test_dir

        _test(codes, input_dir, output_dir)

    def _compile(code_dir: Path, compiled_code_dir: Path):
        codes = list(get_lang(code) for code in code_dir.glob("*") if code.is_file())
        if not codes:
            raise errors.FileNotFound("code")
        for code in codes:
            code.compile(compiled_code_dir)

        return codes

    def _test(codes: List[BaseLanguage], input_dir: Path, output_dir: Path):
        results = _get_output(codes, input_dir, output_dir)

        have_diff = False
        for in_name, output_path_list in results.items():
            diff_output = diff(output_path_list)
            if diff_output:
                have_diff = True
                print(f"  ❌ Test case {in_name}: {diff_output}")

        if not have_diff:
            print("  ✅ There are no differences among your codes' outputs :)")

    def _get_output(codes: List[BaseLanguage], input_dir: Path, output_dir: Path):
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
                _print_progress(
                    input_idx,
                    input_file.name,
                    total_test,
                    code_idx,
                    code.code_path.name,
                    total_code,
                )

                output_path = (
                    output_dir / f"{input_file.stem}_{code.code_path.stem}.ans"
                )
                code.execute(input_file, output_path)
                output_path_list.append(output_path)

            results[input_file.name] = output_path_list

        return results

    def _print_progress(
        test_idx, test_name, total_test, code_idx, code_name, total_code
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
        codes = _compile(env.code_dir, env.target_code_dir)

        print()

        if kind == "all":
            _test_all(codes, env)
        if kind == "sample":
            _test_sample(codes, env)
        elif kind == "handmade":
            _test_handmade(codes, env)
        elif kind == "generated":
            _test_generated(codes, env)

    def _test_all(codes: List[BaseLanguage], env):
        _test_sample(codes, env)
        _test_handmade(codes, env)
        _test_generated(codes, env)

    def _test_sample(codes: List[BaseLanguage], env):
        print("Running your code on sample test cases")

        input_dir = env.sample_test_dir
        output_dir = env.target_sample_test_dir

        _test(codes, input_dir, output_dir)

    def _test_handmade(codes: List[BaseLanguage], env):
        print("Running your code on handmade test cases")

        input_dir = env.handmade_test_dir
        output_dir = env.target_handmade_test_dir

        _test(codes, input_dir, output_dir)

    def _test_generated(codes: List[BaseLanguage], env):
        print("Running your code on generated test cases")

        input_dir = env.generated_test_dir
        output_dir = env.target_generated_test_dir

        _test(codes, input_dir, output_dir)

    def _compile(code_dir: Path, compiled_code_dir: Path):
        codes = list(get_lang(code) for code in code_dir.glob("*") if code.is_file())
        if not codes:
            raise errors.FileNotFound("code")
        for code in codes:
            code.compile(compiled_code_dir)

        return codes

    def _test(codes: List[BaseLanguage], input_dir: Path, output_dir: Path):
        results = _get_output(codes, input_dir, output_dir)

        have_diff = False
        for in_name, output_path_list in results.items():
            diff_output = diff(output_path_list)
            if diff_output:
                have_diff = True
                print(f"  ❌ Test case {in_name}: {diff_output}")

        if not have_diff:
            print("  ✅ There are no differences among your codes' outputs :)")

    def _get_output(codes: List[BaseLanguage], input_dir: Path, output_dir: Path):
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
                _print_progress(
                    input_idx,
                    input_file.name,
                    total_test,
                    code_idx,
                    code.code_path.name,
                    total_code,
                )

                output_path = (
                    output_dir / f"{input_file.stem}_{code.code_path.stem}.ans"
                )
                code.execute(input_file, output_path)
                output_path_list.append(output_path)

            results[input_file.name] = output_path_list

        return results

    def _print_progress(
        test_idx, test_name, total_test, code_idx, code_name, total_code
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
