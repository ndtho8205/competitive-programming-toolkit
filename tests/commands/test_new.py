from pathlib import Path

import pytest

from cptool.commands import NewCommand
from cptool.utils.errors import CptoolError


@pytest.fixture
def new_command():
    return NewCommand()


def test_handle_success(new_command, tmpdir, mocker):
    problem_dir = Path(tmpdir) / "test_problem"
    new_command.handle(problem_dir, interactive=False)


def test_handle_destination_exists_error(new_command, tmpdir, mocker):
    problem_dir = Path(tmpdir) / "test_problem"
    problem_dir.mkdir(parents=True, exist_ok=True)

    with pytest.raises(CptoolError) as e:
        new_command.handle(problem_dir, interactive=False)

    assert e.value.message == f"destination `{problem_dir}` already exists."
