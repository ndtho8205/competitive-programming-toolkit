from pathlib import Path

import pytest

from cptool.cptool import Cptool
from cptool.templates import Template
from cptool.utils.errors import CptoolError


def test_locale_problem_yaml_fail(tmpdir):
    with pytest.raises(CptoolError):
        Cptool.locale_problem_yaml(Path(tmpdir))


def test_locale_problem_yaml_success(tmpdir):
    problem_yaml_file = Path(tmpdir) / "problem.yaml"
    problem_yaml_file.touch()

    got = Cptool.locale_problem_yaml(Path(tmpdir) / "dir1" / "dir2" / "dir3")

    assert got == problem_yaml_file


def test_correct_problem_dir(tmpdir, mocker):
    problem_dir = Path(tmpdir) / "test_problem"
    Template(interactive=False).create(problem_dir)

    dir = problem_dir / "test_cases" / "generated"
    got_problem_yaml_file = Cptool.locale_problem_yaml(dir)
    cptool = Cptool(got_problem_yaml_file)

    assert cptool.codes_dir.absolute() == problem_dir / "codes"
    assert (
        cptool.generated_test_cases_dir.absolute()
        == problem_dir / "test_cases" / "generated"
    )
    assert (
        cptool.handmade_test_cases_dir.absolute()
        == problem_dir / "test_cases" / "handmade"
    )
    assert (
        cptool.examples_test_cases_dir.absolute()
        == problem_dir / "test_cases" / "examples"
    )
    assert (
        cptool.test_cases_generator_file.absolute()
        == problem_dir / "test_cases" / "generator.py"
    )

    assert (
        cptool.compiled_codes_dir.absolute()
        == problem_dir / "target" / "compiled_codes"
    )
    assert (
        cptool.target_generated_test_cases_dir.absolute()
        == problem_dir / "target" / "generated"
    )
    assert (
        cptool.target_handmade_test_cases_dir.absolute()
        == problem_dir / "target" / "handmade"
    )
    assert (
        cptool.target_examples_test_cases_dir.absolute()
        == problem_dir / "target" / "examples"
    )
