from pathlib import Path

import pytest

from cptool.yaml.yaml_file import YamlFile


@pytest.fixture
def yamlfile():
    return YamlFile()


def test_load_from_file(yamlfile):
    yaml_test_file = Path(__file__).parent / "test.yaml"
    content = yamlfile.load(yaml_test_file)

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
    yaml_test_file = Path(__file__).parent / "test.yaml"
    with yaml_test_file.open("r") as f:
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
    raw_file = Path(__file__).parent / "raw_problem.yaml"
    formatted_file = Path(__file__).parent / "formatted_problem.yaml"

    content = yamlfile.load(raw_file)
    dumped_str = yamlfile.dump(content)

    with formatted_file.open("r") as f:
        expected = f.read()

    assert dumped_str == expected
