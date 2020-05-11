from pathlib import Path

import pytest
from ruamel.yaml.scalarstring import FoldedScalarString, LiteralScalarString

from cptool.yaml import ProblemYaml

FIXTURES = Path(__file__).parent / "fixtures"
raw_problem_yaml_file = FIXTURES / "problem.yaml"
formatted_problem_yaml_file = FIXTURES / "formatted_problem.yaml"


@pytest.fixture
def problem_yaml():
    return ProblemYaml()


@pytest.mark.parametrize(
    "input_file,output_file",
    [
        ("problem.yaml", "problem_formatted.yaml"),
        ("problem.yaml", "problem_formatted.yaml"),
        ("problem.yaml", "problem_formatted.yaml"),
    ],
)
def test_load_and_save_file(input_file, output_file, tmpdir):
    got_yaml_file = Path(tmpdir) / "problem.yaml"
    ProblemYaml(FIXTURES / input_file).save(got_yaml_file)

    got = got_yaml_file.read_text(encoding="utf-8")

    want = str(ProblemYaml(FIXTURES / output_file))

    assert got == want
    assert got_yaml_file.exists()


def test_set_basic_info(problem_yaml):
    name = "Problem Test"
    code = "PRBTEST"
    url = "https://www.test.com"

    problem_yaml.set_basic_info(name, code, url)
    content = problem_yaml.content

    assert content["name"] == name
    assert content["code"] == code
    assert content["url"] == url
    assert type(content["name"]) == str
    assert type(content["code"]) == str
    assert type(content["url"]) == str


def test_set_metadata(problem_yaml):
    level = "beginner"
    tags = "DSA"
    contest_name = "DSA"
    contest_code = "DSA"
    contest_url = "https://dsa.com"

    problem_yaml.set_metadata(level, tags, contest_name, contest_url, contest_code)

    metadata = problem_yaml.content["metadata"]

    assert metadata["level"] == level
    assert metadata["tags"] == tags
    assert metadata["contest"]["name"] == contest_name
    assert metadata["contest"]["code"] == contest_code
    assert metadata["contest"]["url"] == contest_url

    assert type(metadata["level"]) == str
    assert type(metadata["tags"]) == str
    assert type(metadata["contest"]["name"]) == str
    assert type(metadata["contest"]["code"]) == str
    assert type(metadata["contest"]["url"]) == str


def test_set_statement(problem_yaml):
    statement = "lorem ipsum"
    input = "1\n2\n"
    output = "1\n2\n"
    constraints = "lorem ipsum"

    problem_yaml.set_statement(statement, input, output, constraints)
    content = problem_yaml.content

    assert content["statement"] == statement
    assert content["input"] == input
    assert content["output"] == output
    assert content["constraints"] == constraints

    assert isinstance(content["statement"], FoldedScalarString)
    assert isinstance(content["input"], FoldedScalarString)
    assert isinstance(content["output"], FoldedScalarString)
    assert isinstance(content["constraints"], FoldedScalarString)


def test_add_examples(problem_yaml):
    input = ""
    output = ""
    explanation = ""

    problem_yaml.add_examples(input, output, explanation)
    content_examples = problem_yaml.content["examples"]

    assert len(content_examples) == 1
    assert content_examples[0]["input"] == input
    assert content_examples[0]["output"] == output
    assert content_examples[0]["explanation"] == explanation

    assert isinstance(content_examples[0]["input"], LiteralScalarString)
    assert isinstance(content_examples[0]["output"], LiteralScalarString)
    assert isinstance(content_examples[0]["explanation"], FoldedScalarString)


def test_export_to_markdown(problem_yaml):
    with pytest.raises(NotImplementedError):
        problem_yaml.export(format="markdown")
