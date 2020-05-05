from io import StringIO

import pytest

from cptool.templates import ProblemYamlGenerator
from cptool.utils.errors import CptoolError
from cptool.yaml import ProblemYaml


@pytest.fixture
def generator():
    return ProblemYamlGenerator("test_problem")


def test_manual_generator_abort(generator, mocker):
    mocker.patch("sys.stdout", new_callable=StringIO)
    mock = mocker.patch("builtins.input")
    mock.side_effect = ["no", "", "", "", "no"]

    with pytest.raises(CptoolError):
        generator.generate()


def test_manual_generator(generator, mocker):
    mocker.patch("sys.stdout", new_callable=StringIO)
    name = "test_problem"
    code = "TESTPROBLEM"
    url = "http://test.com"

    mock = mocker.patch("builtins.input")
    mock.side_effect = ["no", name, code, url, ""]

    got = generator.generate().export()

    default_problem_yaml = ProblemYaml()
    default_problem_yaml.set_basic_info(name, code, url)
    want = default_problem_yaml.export()

    assert got == want


def test_scraping_generator(generator, mocker):
    mocker.patch("sys.stdout", new_callable=StringIO)
    mock = mocker.patch("builtins.input")
    mock.side_effect = ["yes", ""]

    got = generator.generate().export()

    want = ProblemYaml().export()

    assert got == want
