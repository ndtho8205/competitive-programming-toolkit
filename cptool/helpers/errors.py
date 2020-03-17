from pathlib import Path


class Error(Exception):
    message = "Unknown error."

    def get_message(self):
        return f"❗ error: {self.message}"


class CommandNotFound(Error):
    def __init__(self, command: str):
        self.message = f"command `{command}` not found."


class CommandNotImplemented(Error):
    def __init__(self, command: str):
        self.message = f"command `{command}` has not been implemented yet."


class FileNotFound(Error):
    def __init__(self, path: Path):
        self.message = f"`{path}` does not exists."


class NotADirectory(Error):
    def __init__(self, path: Path):
        self.message = f"`{path}` is not a directory."


class DirectoryExists(Error):
    def __init__(self, path: Path):
        self.message = f"destination `{path}` already exists."


class TestgenNotImplemented(Error):
    def __init__(self, path: Path):
        self.message = (
            f"`{path}` must be implemented first before generating test cases."
        )


class LanguageNotSupported(Error):
    def __init__(self, filetype: Path):
        self.message = f"Language `{filetype}` is not supported."
