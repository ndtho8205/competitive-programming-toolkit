from io import StringIO
from pathlib import Path

import pytest

from cptool.commands import NewCommand
from cptool.utils.errors import CptoolError


def test_new_ok(tmpdir, mocker):
    mocker.patch("sys.stdout", new_callable=StringIO)
    mock = mocker.patch("builtins.input")
    mock.side_effect = ["no", "", "", "", "yes"]

    NewCommand().handle(Path(tmpdir) / "test_problem", False)


def test_new_fail(tmpdir, mocker):
    mocker.patch("sys.stdout", new_callable=StringIO)
    mock = mocker.patch("builtins.input")
    mock.side_effect = ["no", "", "", "", "yes"]

    problem_dir = Path(tmpdir) / "test_problem"
    problem_dir.mkdir(parents=True, exist_ok=True)

    with pytest.raises(CptoolError) as e:
        NewCommand().handle(problem_dir, False)
    assert e.value.message == f"destination `{problem_dir}` already exists."
