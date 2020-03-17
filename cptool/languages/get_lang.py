from pathlib import Path

from cptool.languages.languages import CppLanguage, PythonLanguage, RustLanguage
from cptool.helpers import errors


_LANGS = [CppLanguage, PythonLanguage, RustLanguage]

_SUFFIX_LANGS = {suffix: lang for lang in _LANGS for suffix in lang.LANG["suffix"]}


def get_lang(code_path: Path):
    suffix = code_path.suffix
    if suffix not in _SUFFIX_LANGS:
        raise errors.LanguageNotSupported(suffix)
    else:
        return _SUFFIX_LANGS[suffix](code_path)
