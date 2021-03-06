import os
from pathlib import Path

import pytest

from cptool.languages import PythonFile
from cptool.utils import errors

FIXTURES = Path(__file__).parent / "fixtures" / "python"


@pytest.mark.parametrize(
    "code_file", ["execute_fail_divide_zero.py", "execute_fail_undeclared.py"],
)
def test_execute_fail(code_file, tmpdir):
    os.chdir(FIXTURES)
    code_file = Path(code_file)
    _, stderr = read_pipe(code_file)

    with pytest.raises(errors.CodeFileRuntimeError) as e:
        py = PythonFile(code_file)
        py.compile(Path(tmpdir))
        stderr = py.execute()

    assert e.value.stderr == stderr


@pytest.mark.parametrize(
    "code_file", ["execute_success_input_number.py", "execute_success_input_array.py"],
)
def test_execute_success(code_file, tmpdir):
    os.chdir(FIXTURES)
    code_file = Path(code_file)
    stdout, stderr = read_pipe(code_file)
    got_stdout_file = (Path(tmpdir) / code_file).with_suffix(".stdout")

    py = PythonFile(code_file)
    py.compile(Path(tmpdir))
    py.execute(
        input_stream=code_file.with_suffix(".stdin"), output_stream=got_stdout_file
    )

    got_stdout = got_stdout_file.read_text(encoding="utf-8")

    assert stdout == got_stdout


def read_pipe(code_file):
    stdout_pipe = code_file.with_suffix(".stdout").read_text(encoding="utf-8")
    stderr_pipe = code_file.with_suffix(".stderr").read_text(encoding="utf-8")
    return (stdout_pipe, stderr_pipe)
