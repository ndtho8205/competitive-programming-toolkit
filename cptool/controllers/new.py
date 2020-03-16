from pathlib import Path
from shutil import copytree

from cptool.helpers import errors


def new(parent_dir: Path, path: str, template_dir: Path):
    if not parent_dir.exists():
        raise errors.FileNotFound(parent_dir)
    if not parent_dir.is_dir():
        raise errors.NotADirectory(parent_dir)

    problem_dir = parent_dir / path
    if problem_dir.exists() and problem_dir.is_dir():
        raise errors.DirectoryExists(problem_dir)

    print(f"Creating problem in `{problem_dir}`")
    copytree(template_dir, problem_dir)
    print(f"Successfully created problem `{path}`")
