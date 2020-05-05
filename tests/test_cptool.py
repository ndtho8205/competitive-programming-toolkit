from io import StringIO
from pathlib import Path

import pytest

from cptool import Cptool
from cptool.templates import create
from cptool.utils.errors import CptoolError


def test_correct_problem_dir(tmpdir, mocker):
    mocker.patch("sys.stdout", new_callable=StringIO)
    mock = mocker.patch("builtins.input")
    mock.side_effect = ["no", "", "", "", "yes"]

    problem_dir = Path(tmpdir) / "test_problem"
    create(problem_dir)

    cptool = Cptool(problem_dir / "test_cases" / "generated")

    assert cptool.codes_dir() == problem_dir / "codes"
    assert cptool.generated_test_cases_dir() == problem_dir / "test_cases" / "generated"
    assert cptool.handmade_test_cases_dir() == problem_dir / "test_cases" / "handmade"
    assert cptool.examples_test_cases_dir() == problem_dir / "test_cases" / "examples"
    assert (
        cptool.generator_test_cases_file()
        == problem_dir / "test_cases" / "generator.py"
    )


def test_fail_problem_dir(tmpdir):
    with pytest.raises(CptoolError):
        Cptool(Path(tmpdir))
