import subprocess
from pathlib import Path
from typing import List, Optional, Union

from cptool.utils import errors


class BaseCodeFile:
    SUFFIX: List[str] = []

    def __init__(self, code_file: Path):
        self.code_file = code_file
        self.compiled_code_file: Union[Path, None] = None

    def compile_instruction(self, code_file: Path, compiled_code_file: Path):
        raise NotImplementedError()

    def compile(self, compiled_code_file: Path):
        if compiled_code_file.is_dir():
            compiled_code_file = compiled_code_file / self.code_file.stem

        compile_instruction = self.compile_instruction(
            self.code_file, compiled_code_file
        )

        if not compile_instruction:
            return

        retcode, stdout, stderr = self.run(compile_instruction)
        if retcode:
            raise errors.CodeFileCompileError(
                compile_instruction, stderr if stderr else stdout
            )

        self.compiled_code_file = compiled_code_file

    def execute_instruction(self, code_file: Path, compiled_code_file: Optional[Path]):
        return [compiled_code_file]

    def execute(
        self,
        input_stream: Union[Path, str] = None,
        output_stream: Union[Path, None] = None,
    ):
        execute_instruction = self.execute_instruction(
            self.code_file, self.compiled_code_file
        )
        retcode, stdout, stderr = self.run(execute_instruction, input=input_stream)
        if retcode:
            raise errors.CodeFileRuntimeError(
                execute_instruction, stderr if stderr else stdout
            )
        if output_stream:
            output_stream.write_text(stdout, encoding="utf-8")
        return stdout

    def run(
        self,
        args,
        input: Union[str, Path] = None,
        shell: bool = False,
        cwd: Path = None,
        timeout: int = None,
    ):
        if isinstance(input, Path):
            input = input.read_text(encoding="utf-8")

        try:
            result = subprocess.run(
                args,
                shell=shell,
                input=input,
                timeout=timeout,
                encoding="utf-8",
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            return (result.returncode, result.stdout, result.stderr)
        except subprocess.TimeoutExpired:
            return (1, "", "timeout expired.")
