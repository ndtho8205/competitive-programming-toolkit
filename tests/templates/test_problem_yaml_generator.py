import pytest

from cptool.templates import ProblemYamlGenerator
from cptool.yaml import ProblemYaml


@pytest.fixture
def generator():
    return ProblemYamlGenerator("test_problem")


def test_generator(generator):
    got = generator.generate(interactive=False).export()

    default_problem_yaml = ProblemYaml()
    default_problem_yaml.set_basic_info("test_problem")
    want = default_problem_yaml.export()

    assert got == want
