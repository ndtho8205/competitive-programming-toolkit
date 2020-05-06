from io import StringIO
from pathlib import Path

import pytest

from cptool.commands import TestgenCommand
from cptool.templates import Template
from cptool.utils.errors import CptoolError


@pytest.fixture
def testgen_command():
    return TestgenCommand()


@pytest.fixture
def noninteractive_template():
    return Template(interactive=False)


def test_load_generator_file_not_found(testgen_command, tmpdir):
    with pytest.raises(FileNotFoundError):
        testgen_command._load_generator(Path(tmpdir) / "generator.py")


def test_load_generator_success(testgen_command, noninteractive_template, tmpdir):
    problem_dir = Path(tmpdir)
    generator_file = Path(tmpdir) / "test_cases" / "generator.py"

    noninteractive_template.create_test_cases_generator(problem_dir)

    testgen_command._load_generator(generator_file)


def test_handle_fail(testgen_command, noninteractive_template, tmpdir, mocker):
    problem_dir = Path(tmpdir) / "test_problem"
    noninteractive_template.create(problem_dir)

    mocker.patch.object(Path, "cwd", return_value=problem_dir)

    with pytest.raises(CptoolError):
        testgen_command.handle(10)


def test_handle_success(testgen_command, noninteractive_template, tmpdir, mocker):
    problem_dir = Path(tmpdir) / "test_problem"
    noninteractive_template.create(problem_dir)

    generator_file = problem_dir / "test_cases" / "generator.py"
    generator_content = """\
def generate(f_rand):
    return f_rand(0, 10)
    """
    with generator_file.open("w") as f:
        f.write(generator_content)

    mocker.patch.object(Path, "cwd", return_value=problem_dir)
    testgen_command.handle(10)

    assert len(list((problem_dir / "test_cases" / "generated").glob("*"))) == 10
