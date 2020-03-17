import subprocess
from pathlib import Path

from cptool.helpers import errors


class BaseLanguage:
    LANG = {
        "suffix": [],
        "compile": "",
        "execute": "",
    }

    def __init__(self, code_path: Path):
        if not (code_path.exists() and code_path.is_file()):
            raise errors.FileNotFound(code_path)

        if code_path.suffix not in self.LANG["suffix"]:
            raise errors.LanguageNotSupported(code_path.suffix)

        self.code_path = code_path
        self.compiled_path = None

    def compile(self, output_dir: Path):
        compile_instruction = self.LANG["compile"]
        if not compile_instruction:
            print(f"`{self.code_path}` don't need to compile.")
            return

        output_dir.mkdir(parents=True, exist_ok=True)

        self.compiled_path = output_dir / self.code_path.stem

        try:
            subprocess.check_call(
                self.LANG["compile"].format(
                    input=self.code_path, output=self.compiled_path
                ),
                shell=True,
            )
        except subprocess.CalledProcessError:
            raise errors.CompileError(self.code_path)

        print(
            f"Successfully compiled file `{self.code_path}` in `{self.compiled_path}`"
        )

    def execute(self, input_file: Path, output_file: Path):
        try:
            subprocess.check_call(
                self.LANG["execute"].format(
                    self.compiled_path, input_file, output_file
                ),
                shell=True,
            )
        except subprocess.CalledProcessError:
            raise errors.ExecuteError(self.code_path, input_file, output_file)


class CppLanguage(BaseLanguage):
    LANG = {
        "suffix": [".cpp"],
        "compile": "g++ '{input}' -o '{output}'",
        "execute": "./{} < {} > {}",
    }


class PythonLanguage(BaseLanguage):
    LANG = {
        "suffix": [".py"],
        "compile": "",
        "execute": "python3 {} < {} > {}",
    }

    def compile(self, output_dir: Path):
        super().compile(output_dir)
        self.compiled_path = self.code_path


class RustLanguage(BaseLanguage):
    LANG = {
        "suffix": [".rs"],
        "compile": "rustc '{input}' -o '{output}'",
        "execute": "./{} < {} > {}",
    }
