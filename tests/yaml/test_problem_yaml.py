from pathlib import Path

import pytest

from cptool.yaml import ProblemYaml

FIXTURES = Path(__file__).parent / "fixtures"
raw_problem_yaml_file = FIXTURES / "raw_problem.yaml"
formatted_problem_yaml_file = FIXTURES / "formatted_problem.yaml"


@pytest.mark.parametrize(
    "input_file,output_file", [(raw_problem_yaml_file, formatted_problem_yaml_file)],
)
def test_load_and_save_file(input_file, output_file):
    got = ProblemYaml(input_file).export()
    want = ProblemYaml(output_file).export()
    assert got == want
