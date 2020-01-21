from pathlib import Path
from shutil import copytree

from src import config


def create(parent_dir: Path, problem_name: str):
    if not parent_dir.exists():
        raise FileNotFoundError(f"{parent_dir} does not exists.")
    if not parent_dir.is_dir():
        raise NotADirectoryError(f"{parent_dir} is not a directory.")

    problem_dir = parent_dir / problem_name
    if problem_dir.exists() and problem_dir.is_dir():
        raise FileExistsError(f"{problem_dir} already exists.")

    print(f"Creating problem in {problem_dir}")
    copytree(config.TEMPLATE_PATH, problem_dir)
    print(f"Successfully created problem {problem_name}")
