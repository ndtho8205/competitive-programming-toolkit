from pathlib import Path

import pytest

from cptool.commands import CheckCommand
from cptool.templates import Template
from cptool.utils.errors import CptoolError


@pytest.fixture
def check_command():
    return CheckCommand()


def test_handle_success(check_command, tmpdir, mocker):
    return
    problem_dir = Path(tmpdir) / "test_problem"
    Template(interactive=False).create_problem_yaml(problem_dir)

    mocker.patch.object(Path, "cwd", return_value=problem_dir)
    check_command.handle()


def test_handle_fail(check_command, tmpdir, mocker):
    problem_dir = Path(tmpdir) / "test_problem"
    problem_dir.mkdir(parents=True, exist_ok=True)

    mocker.patch.object(Path, "cwd", return_value=problem_dir)
    with pytest.raises(CptoolError):
        check_command.handle()
