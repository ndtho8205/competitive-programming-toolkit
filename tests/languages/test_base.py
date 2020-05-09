from pathlib import Path

import pytest

from cptool.languages import BaseCodeFile


class TestFile(BaseCodeFile):
    pass


def test_compile_instruction(tmpdir):
    with pytest.raises(NotImplementedError):
        TestFile(Path(tmpdir)).compile_instruction(tmpdir, tmpdir)
