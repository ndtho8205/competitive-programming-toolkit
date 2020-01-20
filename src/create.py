from pathlib import Path
from shutil import copytree

from src import config


def create(parent_path: Path, problem_name: str):
    if not parent_path.exists():
        raise FileNotFoundError(f"{parent_path} does not exists.")
    if not parent_path.is_dir():
        raise NotADirectoryError(f"{parent_path} is not a directory.")

    problem_path = parent_path / problem_name
    if (problem_path).exists():
        raise FileExistsError(f"{problem_path} already exists.")

    print(f"Creating problem in {problem_path}")
    copytree(config.TEMPLATE_PATH, problem_path)
    print(f"Successfully created problem {problem_name}")
