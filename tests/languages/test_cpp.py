import os
from pathlib import Path

import pytest

from cptool.languages import CppFile
from cptool.utils import errors

FIXTURES = Path(__file__).parent / "fixtures" / "cpp"


@pytest.mark.parametrize(
    "code_file",
    [
        "compile_fail_divide_zero.cpp",
        "compile_fail_std.cpp",
        "compile_fail_undeclared.cpp",
    ],
)
def test_compile_fail(code_file, tmpdir):
    os.chdir(FIXTURES)
    code_file = Path(code_file)
    _, stderr = read_pipe(code_file)

    with pytest.raises(errors.CodeFileCompileError) as e:
        CppFile(code_file).compile(Path(tmpdir))

    assert e.value.stderr == stderr


@pytest.mark.parametrize(
    "code_file",
    ["execute_success_input_number.cpp", "execute_success_input_string.cpp"],
)
def test_execute_success(code_file, tmpdir):
    os.chdir(FIXTURES)
    code_file = Path(code_file)
    stdout, stderr = read_pipe(code_file)

    cpp = CppFile(code_file)
    cpp.compile(Path(tmpdir))
    got_stdout = cpp.execute(
        input_stream=code_file.with_suffix(".stdin"), output_stream=None
    )

    assert stdout == got_stdout


def read_pipe(code_file):
    stdout_pipe = code_file.with_suffix(".stdout").read_text(encoding="utf-8")
    stderr_pipe = code_file.with_suffix(".stderr").read_text(encoding="utf-8")
    return (stdout_pipe, stderr_pipe)
