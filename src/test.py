from typing import List, Tuple
from pathlib import Path

from src import config, compiler


def _get_code_path_list(code_dir: Path):
    # TODO: process other files than C++
    return list(code_dir.glob("*.cpp"))


def _print_progress(test_idx, test_name, total_test, code_idx, code_name, total_code):
    print(
        "".join(
            [
                f"\r  {test_idx + 1}/{total_test} test cases - ",
                f"{code_idx + 1}/{total_code} codes: {code_name} on {test_name}",
            ]
        ),
        end="",
    )


def _test(
    compiled_code_list: List[Tuple[dict, Path]], test_dir: Path, output_dir: Path
):
    # TODO: support different filename pattern
    output_dir.mkdir(parents=True, exist_ok=True)

    total_test = len(list(test_dir.glob("*.in")))
    total_code = len(compiled_code_list)

    results = {}
    for in_idx, in_path in enumerate(test_dir.glob("*.in")):
        for code_idx, (lang, compiled_code_path) in enumerate(compiled_code_list):
            _print_progress(
                in_idx,
                in_path.name,
                total_test,
                code_idx,
                compiled_code_path.name,
                total_code,
            )

            output_path = output_dir / f"{in_path.stem}_{compiled_code_path.stem}.ans"
            compiler.execute(lang, compiled_code_path, in_path, output_path)

            if compiled_code_path.name in results:
                results[compiled_code_path.name].append(output_path)
            else:
                results[compiled_code_path.name] = [output_path]

    return results


def test(problem_dir: Path):
    code_dir = problem_dir / config.PROBLEM_PATH["code"]

    sample_test_dir = problem_dir / config.PROBLEM_PATH["sample_test"]
    handmade_test_dir = problem_dir / config.PROBLEM_PATH["handmade_test"]
    generated_test_dir = problem_dir / config.PROBLEM_PATH["generated_test"]

    temp_dir = problem_dir / config.PROBLEM_PATH["temp"]
    output_sample_test_dir = temp_dir / config.PROBLEM_PATH["sample_test"]
    output_handmade_test_dir = temp_dir / config.PROBLEM_PATH["handmade_test"]
    output_generated_test_dir = temp_dir / config.PROBLEM_PATH["generated_test"]

    # compiled_code_list = List[(lang, compiled_code_path)]
    compiled_code_list = list(
        map(
            lambda code_path: compiler.compile(
                code_path,
                compiled_output_dir=problem_dir
                / config.PROBLEM_PATH["temp"]
                / config.PROBLEM_PATH["code"],
            ),
            _get_code_path_list(code_dir),
        )
    )
    print()

    print("Running your code on sample test cases")
    sample_results = _test(compiled_code_list, sample_test_dir, output_sample_test_dir)
    print()

    print("Running your code on handmade test cases")
    handmade_results = _test(
        compiled_code_list, handmade_test_dir, output_handmade_test_dir
    )
    print()

    print("Running your code on generated test cases")
    generated_results = _test(
        compiled_code_list, generated_test_dir, output_generated_test_dir
    )
    print()

    print(sample_results)
    print(handmade_results)
    print(generated_results)
