from pathlib import Path

from cptool.languages import BaseCodeFile


class RustFile(BaseCodeFile):
    SUFFIX = [".rs"]

    def compile_instruction(self, code_file: Path, compiled_code_file: Path):
        return ["rustc", code_file, "-o", compiled_code_file]
