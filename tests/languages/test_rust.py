import os
from pathlib import Path

import pytest

from cptool.languages import RustFile
from cptool.utils import errors

FIXTURES = Path(__file__).parent / "fixtures" / "rust"


@pytest.mark.parametrize(
    "code_file", ["compile_fail_macro.rs"],
)
def test_compile_fail(code_file, tmpdir):
    os.chdir(FIXTURES)
    code_file = Path(code_file)
    _, stderr = read_pipe(code_file)

    with pytest.raises(errors.CodeFileCompileError) as e:
        RustFile(code_file).compile(Path(tmpdir))

    assert e.value.stderr == stderr


@pytest.mark.parametrize(
    "code_file", ["execute_success_input_string.rs"],
)
def test_execute_success(code_file, tmpdir):
    os.chdir(FIXTURES)
    code_file = Path(code_file)
    stdout, stderr = read_pipe(code_file)

    rs = RustFile(code_file)
    rs.compile(Path(tmpdir))
    got_stdout = rs.execute(
        input_stream=code_file.with_suffix(".stdin"), output_stream=None
    )

    assert stdout == got_stdout


def read_pipe(code_file):
    with code_file.with_suffix(".stdout").open("r") as f:
        stdout_pipe = f.read()

    with code_file.with_suffix(".stderr").open("r") as f:
        stderr_pipe = f.read()

    return (stdout_pipe, stderr_pipe)
