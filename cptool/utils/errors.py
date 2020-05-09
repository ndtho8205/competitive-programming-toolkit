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


class CodeFileCompileError(Error):
    def __init__(self, cmd, stderr):
        self.message = f"cannot compile `{cmd}`"
        self.stderr = stderr


class CodeFileRuntimeError(Error):
    def __init__(self, cmd, stderr):
        self.message = f"fail to run `{cmd}`"
        self.stderr = stderr


class CodeFileTimeoutExpiredError(Error):
    def __init__(self, cmd, timeout, stdout, stderr):
        self.message = "".join()
