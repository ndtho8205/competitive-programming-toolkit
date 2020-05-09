from io import StringIO
from pathlib import Path

import pytest

from cptool.templates import Template
from cptool.templates.template import TEST_CASE_GENERATOR_DEFAULT
from cptool.yaml import ProblemYaml
from cptool.utils.errors import CptoolError

PROBLEM_NAME = "test_problem"


@pytest.fixture
def interactive_template():
    return Template(interactive=True)


@pytest.fixture
def noninteractive_template():
    return Template(interactive=False)


def test_create_structure(interactive_template, tmpdir):
    problem_dir = Path(tmpdir) / PROBLEM_NAME

    interactive_template.create_structure(problem_dir)

    assert (problem_dir / "codes").exists()
    assert (problem_dir / "test_cases").exists()
    assert (problem_dir / "test_cases" / "generated").exists()
    assert (problem_dir / "test_cases" / "handmade").exists()
    assert (problem_dir / "test_cases" / "examples").exists()


def test_create_test_cases_generator(interactive_template, tmpdir):
    problem_dir = Path(tmpdir) / PROBLEM_NAME

    interactive_template.create_test_cases_generator(problem_dir)

    generator_file = problem_dir / "test_cases" / "generator.py"
    assert generator_file.exists()

    with generator_file.open("r") as f:
        content = f.read()
    assert content == TEST_CASE_GENERATOR_DEFAULT


def test_interactive_create_problem_yaml_manual(interactive_template, tmpdir, mocker):
    problem_dir = Path(tmpdir) / PROBLEM_NAME
    problem_code = "TESTPROBLEM"
    problem_url = "http://test.problem.com"

    mocker.patch("sys.stdout", new_callable=StringIO)
    mock = mocker.patch("builtins.input")
    mock.side_effect = [
        "no",  # extract problem information from URL?
        PROBLEM_NAME,  # problem name?
        problem_code,  # problem_code?
        problem_url,  # problem_url?
        "yes",  # generate?
    ]
    interactive_template.create_problem_yaml(problem_dir)

    problem_yaml_file = problem_dir / "problem.yaml"
    assert problem_yaml_file.exists()

    content = ProblemYaml(problem_yaml_file).content
    assert content["name"] == PROBLEM_NAME
    assert content["code"] == problem_code
    assert content["url"] == problem_url


def test_interactive_create_problem_yaml_aborted_error(
    interactive_template, tmpdir, mocker
):
    problem_dir = Path(tmpdir) / PROBLEM_NAME

    mocker.patch("sys.stdout", new_callable=StringIO)
    mock = mocker.patch("builtins.input")
    mock.side_effect = [
        "no",  # extract problem information from URL?
        PROBLEM_NAME,  # problem name?
        "",  # problem_code?
        "",  # problem_url?
        "no",  # generate?
    ]

    with pytest.raises(CptoolError):
        interactive_template.create_problem_yaml(problem_dir)


def test_interactive_create_problem_yaml_scrape(interactive_template, tmpdir, mocker):
    problem_dir = Path(tmpdir) / PROBLEM_NAME

    mocker.patch("sys.stdout", new_callable=StringIO)
    mock = mocker.patch("builtins.input")
    mock.side_effect = [
        "yes",  # extract problem information from URL?
        "yes",  # generate?
    ]
    interactive_template.create_problem_yaml(problem_dir)

    problem_yaml_file = problem_dir / "problem.yaml"
    assert problem_yaml_file.exists()

    content = ProblemYaml(problem_yaml_file).content
    assert content["name"] == ""


def test_noninteractive_create_problem_yaml(noninteractive_template, tmpdir):
    problem_dir = Path(tmpdir) / PROBLEM_NAME

    noninteractive_template.create_problem_yaml(problem_dir)

    problem_yaml_file = problem_dir / "problem.yaml"
    assert problem_yaml_file.exists()

    content = ProblemYaml(problem_yaml_file).content
    assert content["name"] == PROBLEM_NAME


def test_noninteractive_create(noninteractive_template, tmpdir):
    problem_dir = Path(tmpdir) / PROBLEM_NAME

    noninteractive_template.create(problem_dir)


def test_interactive_create(interactive_template, tmpdir, mocker):
    mocker.patch("sys.stdout", new_callable=StringIO)
    mock = mocker.patch("builtins.input")
    mock.side_effect = ["no", "", "", "", "yes"]

    problem_name = "test_problem"
    problem_dir = Path(tmpdir) / problem_name
    interactive_template.create(problem_dir)

    assert (problem_dir / "codes").exists()
    assert (problem_dir / "test_cases").exists()
    assert (problem_dir / "test_cases" / "generated").exists()
    assert (problem_dir / "test_cases" / "handmade").exists()
    assert (problem_dir / "test_cases" / "examples").exists()
    assert (problem_dir / "test_cases" / "generator.py").exists()
    assert (problem_dir / "README.md").exists()
    assert (problem_dir / "problem.yaml").exists()
