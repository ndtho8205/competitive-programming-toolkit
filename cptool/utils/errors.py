from pathlib import Path
from typing import List


class Error(Exception):
    message = "Unknown error."

    def get_message(self):
        return f"❗ error: {self.message}"


class CptoolError(Error):
    def __init__(self, message):
        self.message = message


class NotFoundKey(Error):
    def __init__(self, keys: List[str]):
        self.message = "not found keys: {}".format(", ".join(keys))


class UnsupportedKey(Error):
    def __init__(self, keys: List[str]):
        self.message = "key type: {}".format(", ".join(keys))


class KeyTypeError(Error):
    def __init__(self, key: str, expected_type: str):
        self.message = f"key `{key}` should be a `{expected_type}`."


class TestgenNotImplemented(Error):
    def __init__(self, path: Path):
        self.message = (
            f"`{path}` must be implemented first before generating test cases."
        )


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
