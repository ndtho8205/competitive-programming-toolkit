from pathlib import Path

from cptool.languages.cpp import CppFile
from cptool.languages.python import PythonFile
from cptool.languages.rust import RustFile
from cptool.utils.errors import CptoolError

_LANGS = [CppFile, PythonFile, RustFile]
_SUFFIX_LANGS = {suffix: lang for lang in _LANGS for suffix in lang.SUFFIX}


def get_lang(code_file: Path):
    suffix = code_file.suffix
    if suffix not in _SUFFIX_LANGS:
        raise CptoolError(f"language used in `{code_file}` is not supported")

    return _SUFFIX_LANGS[suffix](code_file)
