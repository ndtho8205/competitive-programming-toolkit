from pathlib import Path

import pytest

from cptool.languages import get_lang
from cptool.utils.errors import CptoolError


@pytest.mark.parametrize("code_file", ["test.py", "test.cpp", "test.rs"])
def test_get_lang_success(code_file):
    get_lang(Path(code_file))


@pytest.mark.parametrize("code_file", ["test.doc", "test.xls"])
def test_get_lang_fail(code_file):
    with pytest.raises(CptoolError):
        get_lang(Path(code_file))
