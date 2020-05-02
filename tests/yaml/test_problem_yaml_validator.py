import pytest

from cptool.utils.errors import KeyTypeError, NotFoundKey, UnsupportedKey
from cptool.yaml import ProblemYamlValidator

expected_content = """\
name:
metadata:
  level:
  contest:
    name:
input: >
"""


@pytest.fixture
def validator():
    return ProblemYamlValidator(expected_content)


def test_correct(validator):
    pass
    # validator.validate(expected_content)


@pytest.mark.parametrize(
    "content,expected_errs",
    [
        ("name:\nmetadata:\n  level:\n  contest:\n    name:\n", NotFoundKey(["input"])),
        (
            "name:\ninput: >\nmetadata:\n  contest:\n",
            NotFoundKey(["metadata.level", "metadata.contest.name"]),
        ),
        (
            "name:\ninput:\nmetadata:\n  level:\n  contest:\n    name:\n",
            KeyTypeError("input", "folded string, indicated by >"),
        ),
    ],
)
def test_missing_keys(validator, content, expected_errs):
    with pytest.raises(expected_errs.__class__) as e:
        validator.validate(content)
    assert type(e.value) == type(expected_errs)
    assert e.value.message == expected_errs.message
