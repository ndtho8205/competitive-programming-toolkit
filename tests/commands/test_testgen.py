from io import StringIO
from pathlib import Path

import pytest

from cptool.commands import TestgenCommand
from cptool.templates import create
from cptool.utils.errors import CptoolError


@pytest.fixture
def testgen():
    return TestgenCommand()


def test_load_generator_file_not_found(testgen, tmpdir):
    with pytest.raises(FileNotFoundError):
        testgen._load_generator(Path(tmpdir) / "generator.py")


def test_load_generator_success(testgen, tmpdir):
    generator_file = Path(tmpdir) / "generator.py"
    generator_content = """\
def generate(f_rand):
    raise NotImplementedError()
"""
    with generator_file.open("w") as f:
        f.write(generator_content)

    testgen._load_generator(generator_file)


def test_testgen_command(testgen, tmpdir, mocker):
    mocker.patch("sys.stdout", new_callable=StringIO)
    mock = mocker.patch("builtins.input")
    mock.side_effect = ["no", "", "", "", "yes"]

    problem_dir = Path(tmpdir) / "test_problem"
    mocker.patch.object(Path, "cwd", return_value=problem_dir)

    create(problem_dir)

    with pytest.raises(CptoolError):
        testgen.handle(10)

    generator_file = problem_dir / "test_cases" / "generator.py"
    generator_content = """\
def generate(f_rand):
    return f_rand(0, 10)
    """
    with generator_file.open("w") as f:
        f.write(generator_content)

    testgen.handle(10)

    assert len(list((problem_dir / "test_cases" / "generated").glob("*"))) == 10
