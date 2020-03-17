from typing import List
from pathlib import Path

from cptool.languages import BaseLanguage, get_lang
from cptool.helpers import diff


def test_all(env):
    test_sample(env)
    test_handmade(env)
    test_generated(env)


def test_sample(env):
    print("Running your code on sample test cases")

    codes = _compile(env.code_dir, env.target_code_dir)
    input_dir = env.sample_test_dir
    output_dir = env.target_sample_test_dir

    _test(codes, input_dir, output_dir)


def test_handmade(env):
    print("Running your code on handmade test cases")

    codes = _compile(env.code_dir, env.target_code_dir)
    input_dir = env.handmade_test_dir
    output_dir = env.target_handmade_test_dir

    _test(codes, input_dir, output_dir)


def test_generated(env):
    print("Running your code on generated test cases")

    codes = _compile(env.code_dir, env.target_code_dir)
    input_dir = env.generated_test_dir
    output_dir = env.target_generated_test_dir

    _test(codes, input_dir, output_dir)


def _compile(code_dir: Path, compiled_code_dir: Path):
    codes = list(get_lang(code) for code in code_dir.glob("*") if code.is_file())
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
        print("  ✅ There is no difference among your codes' outputs :)")


def _get_output(codes: List[BaseLanguage], input_dir: Path, output_dir: Path):
    # TODO: support different filename pattern
    output_dir.mkdir(parents=True, exist_ok=True)

    total_code = len(codes)
    total_test = len(list(input_dir.glob("*.in")))

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

            output_path = output_dir / f"{input_file.stem}_{code.code_path.stem}.ans"
            code.execute(input_file, output_path)
            output_path_list.append(output_path)

        results[input_file.name] = output_path_list

    return results


def _print_progress(test_idx, test_name, total_test, code_idx, code_name, total_code):
    if test_idx + 1 == total_test and code_idx + 1 == total_code:
        print(f"\r\x1b[2K  {total_test}/{total_test} test cases are tested.")
    else:
        print(
            "".join(
                [
                    f"\r  Test case {test_idx + 1}/{total_test} > ",
                    f"Code {code_idx + 1}/{total_code} >> {code_name} on {test_name}",
                ]
            ),
            end="",
        )
