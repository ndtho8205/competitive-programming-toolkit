from pathlib import Path

import pytest

from cptool.utils.errors import KeyTypeError, NotFoundKeyError, UnsupportedKeyError
from cptool.yaml import YAML_DEFAULT, ProblemYamlValidator

FIXTURES = Path(__file__).parent / "fixtures"


@pytest.fixture
def validator():
    return ProblemYamlValidator()


@pytest.mark.parametrize(
    "content",
    [
        FIXTURES / "problem.yaml",
        FIXTURES / "problem_formatted.yaml",
        FIXTURES / "validator_empty_examples.yaml",
        FIXTURES / "validator_empty_name.yaml",
        YAML_DEFAULT,
    ],
)
def test_correct(content):
    ProblemYamlValidator().validate(content)


@pytest.mark.parametrize(
    "content",
    [
        "validator_NotFoundKey_url.yaml",
        "validator_NotFoundKey_examples[1].input.yaml",
        "validator_NotFoundKey_metadata.contest.name.yaml",
        "validator_NotFoundKey_metadata.tags.yaml",
        "validator_UnsupportedKey_examples[1].random.yaml",
        "validator_UnsupportedKey_metadata.contest.random.yaml",
        "validator_UnsupportedKey_metadata.random.yaml",
        "validator_UnsupportedKey_random.yaml",
    ],
)
def test_invalid_key(validator, content):
    content_file = FIXTURES / content

    expected_error_key = [content_file.stem.split("_")[2]]
    expected_error = (
        NotFoundKeyError
        if content_file.stem.split("_")[1] == "NotFoundKey"
        else UnsupportedKeyError
    )(expected_error_key)

    with pytest.raises(expected_error.__class__) as got_error:
        validator.validate(content_file)

    assert type(got_error.value) == type(expected_error)
    assert got_error.value.message == expected_error.message


@pytest.mark.parametrize(
    "content",
    [
        "validator_KeyType_examples[0].explanation_folded.yaml",
        "validator_KeyType_examples[0].input_literal.yaml",
        "validator_KeyType_metadata.contest.name_str.yaml",
        "validator_KeyType_metadata.level_str.yaml",
        "validator_KeyType_name_str.yaml",
    ],
)
def test_invalid_key_type(validator, content):
    content_file = FIXTURES / content

    expected_error = KeyTypeError(
        content_file.stem.split("_")[2], content_file.stem.split("_")[3],
    )

    with pytest.raises(expected_error.__class__) as got_error:
        validator.validate(content_file)

    assert type(got_error.value) == type(expected_error)
    assert got_error.value.message.startswith(expected_error.message[:-2])
