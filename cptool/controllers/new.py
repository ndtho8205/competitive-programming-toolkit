from pathlib import Path
from shutil import copytree

from cptool.helpers import config


def new(parent_dir: Path, path: str):
    if not parent_dir.exists():
        raise FileNotFoundError(f"{parent_dir} does not exists.")
    if not parent_dir.is_dir():
        raise NotADirectoryError(f"{parent_dir} is not a directory.")

    problem_dir = parent_dir / path
    if problem_dir.exists() and problem_dir.is_dir():
        raise FileExistsError(f"{problem_dir} already exists.")

    print(f"Creating problem in {problem_dir}")
    copytree(config.TEMPLATE_PATH, problem_dir)
    print(f"Successfully created problem {path}")
