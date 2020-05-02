import pytest

from cptool.utils.errors import KeyTypeError, NotFoundKey, UnsupportedKey
from cptool.yaml import YAML_DEFAULT, ProblemYamlValidator

expected_content = """\
name: ''
meta:
  tags:
    - foo: 0
      bar: 1
  cont:
    dis: |
inp: >
"""


@pytest.fixture
def validator():
    return ProblemYamlValidator(expected_content)


@pytest.mark.parametrize(
    "content", [expected_content, YAML_DEFAULT],
)
def test_correct(validator, content):
    ProblemYamlValidator(content).validate(content)


@pytest.mark.parametrize(
    "content,expected_errs",
    [
        (
            "cat:\nname: ''\nmeta:\n  tags:\n    - foo: 0\n      bar: 1\n  cont:\n    dis: |\ninp: >\n",
            UnsupportedKey(["cat"]),
        ),
        (
            "meta:\n  tags:\n    - foo: 0\n      bar: 1\n  cont:\n    dis: |\ninp: >\n",
            NotFoundKey(["name"]),
        ),
        (
            "name: ''\nmeta:\n  tags:\n    - foo: 0\n      bar: 1\ninp: >\n",
            NotFoundKey(["meta.cont"]),
        ),
    ],
)
def test_missing_keys(validator, content, expected_errs):
    with pytest.raises(expected_errs.__class__) as e:
        validator.validate(content)
    assert type(e.value) == type(expected_errs)
    assert e.value.message == expected_errs.message


@pytest.mark.parametrize(
    "content,expected_errs",
    [
        (
            "name: ''\nmeta:\n  tags:\n    - foo: 0\n      bar: 1\n  cont:\n    dis: |\ninp: \n",
            KeyTypeError("inp", "folded string, indicated by >"),
        ),
        (
            "name: ''\nmeta:\n  tags:\n    - foo: 0\n      bar: 1\n  cont:\n    dis: \ninp: >\n",
            KeyTypeError("dis", "literal string, indicated by |"),
        ),
        (
            "name: \nmeta:\n  tags:\n    - foo: 0\n      bar: 1\n  cont:\n    dis: |\ninp: >\n",
            KeyTypeError("name", "string"),
        ),
        (
            "name: ''\nmeta:\n  tags:\n  cont:\n    dis: |\ninp: >\n",
            KeyTypeError("tags", "list"),
        ),
    ],
)
def test_wrong_type_keys(validator, content, expected_errs):
    with pytest.raises(expected_errs.__class__) as e:
        validator.validate(content)
    assert type(e.value) == type(expected_errs)
    assert e.value.message == expected_errs.message
