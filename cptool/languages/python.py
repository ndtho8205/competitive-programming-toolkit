from pathlib import Path

from cptool.languages import BaseCodeFile


class PythonFile(BaseCodeFile):
    SUFFIX = [".py"]

    def compile_instruction(self, code_file: Path, compiled_code_file: Path):
        return None

    def execute_instruction(self, code_file: Path, compiled_code_file: Path):
        return ["python3", code_file]
