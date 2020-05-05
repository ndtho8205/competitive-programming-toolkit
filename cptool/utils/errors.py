from pathlib import Path
from typing import List, Union


class Error(Exception):
    message = "Unknown error."

    def get_message(self):
        return f"❗ error: {self.message}"


class CptoolError(Error):
    def __init__(self, message):
        self.message = message


class NotFoundKeyError(Error):
    def __init__(self, keys: Union[str, List[str]]):
        self.message = "problem.yaml is invalid: not found key(s):\n  {}".format(
            "\n  ".join(keys)
        )


class UnsupportedKeyError(Error):
    def __init__(self, keys: Union[str, List[str]]):
        self.message = "problem.yaml is invalid: unsupported key(s):\n  {}".format(
            "\n   ".join(keys)
        )


class KeyTypeError(Error):
    def __init__(self, key: str, want: str):
        self.message = f"problem.yaml is invalid: `{key}` should have type `{want}`."


class LanguageNotSupported(Error):
    def __init__(self, filetype: Path):
        self.message = f"language `{filetype}` is not supported."


class CompileError(Error):
    def __init__(self, code_path: Path):
        self.message = f"cannot compile `{code_path}`."


class ExecuteError(Error):
    def __init__(self, code_path: Path, input_file: Path, output_file: Path):
        self.message = "".join(
            [
                f"executing `{code_path}` with input `{input_file}` ",
                f"and output `{output_file}` was aborted.",
            ]
        )
