from pathlib import Path

import pytest

from cptool.utils.yaml_file import YamlFile

FIXTURES = Path(__file__).parent / "fixtures"
test_yaml_file = FIXTURES / "test.yaml"
raw_problem_yaml_file = FIXTURES / "raw_problem.yaml"
formatted_problem_yaml_file = FIXTURES / "formatted_problem.yaml"


@pytest.fixture
def yamlfile():
    return YamlFile()


def test_load_from_file(yamlfile):
    content = yamlfile.load(test_yaml_file)

    assert content["title"] == "YAML Example"

    assert content["special"] == "あ"

    assert len(content["stuff"]) == 2
    assert content["stuff"][0]["foo"] == "bar"
    assert content["stuff"][1] == "bar"

    assert (
        content["foo"]
        == "this is not a normal string it spans more than one line\nsee?\n"
    )


def test_load_from_str(yamlfile):
    content = yamlfile.load(
        """
        foo: bar
        """
    )
    assert content["foo"] == "bar"


def test_load_from_stream(yamlfile):
    with test_yaml_file.open("r") as f:
        content = yamlfile.load(f)

    assert content["title"] == "YAML Example"


@pytest.mark.parametrize(
    "content,expected",
    [
        (dict(foo="bar"), "foo: bar\n"),
        (dict(foo=["bar", "bop"]), "foo:\n  - bar\n  - bop\n"),
        (dict(foo=dict(bar=["bop", "zoo"])), "foo:\n  bar:\n    - bop\n    - zoo\n"),
    ],
)
def test_dump_to_str(yamlfile, content, expected):
    assert yamlfile.dump(content, None) == expected


@pytest.mark.parametrize(
    "content,expected",
    [
        ("foo: |\n  hello\n  world\n\n", "foo: |\n  hello\n  world\n\n"),
        (
            "foo: >-2\nbar: >-2\n  hello\n  world\n\n  !",
            "foo: >\nbar: >-\n  hello\n  world\n\n  !\n",
        ),
    ],
)
def test_folded_and_literal(yamlfile, content, expected):
    dumped_str = yamlfile.dump(yamlfile.load(content), None)
    assert dumped_str == expected


def test_problem_yaml(yamlfile):
    content = yamlfile.load(raw_problem_yaml_file)
    dumped_str = yamlfile.dump(content)

    with formatted_problem_yaml_file.open("r") as f:
        expected = f.read()

    assert dumped_str == expected
