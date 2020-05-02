from pathlib import Path

from cptool.templates.template import create


def test_create(tmpdir):
    problem_name = "test_problem"
    problem_dir = Path(tmpdir) / problem_name
    create(problem_dir, interactive=False)

    assert (problem_dir / "codes").exists()
    assert (problem_dir / "test_cases").exists()
    assert (problem_dir / "test_cases" / "generated").exists()
    assert (problem_dir / "test_cases" / "handmade").exists()
    assert (problem_dir / "test_cases" / "examples").exists()
    assert (problem_dir / "test_cases" / "generator.py").exists()
    assert (problem_dir / "README.md").exists()
    assert (problem_dir / "problem.yaml").exists()