from collections import OrderedDict
from pathlib import Path
from typing import Union

from ruamel.yaml.scalarstring import FoldedScalarString, LiteralScalarString

from cptool.utils import YamlFile
from cptool.utils.errors import KeyTypeError, NotFoundKeyError, UnsupportedKeyError
from cptool.yaml.default import YAML_DEFAULT


class ProblemYamlValidator:
    def __init__(self):
        self._expected = YamlFile().load(YAML_DEFAULT)

    def validate(self, problem_yaml: Union[Path, str]):
        content = YamlFile().load(problem_yaml)

        self._validate(content, self._expected)

        return True

    def _validate(self, got, want, key: str = ""):
        if got is None:
            return

        if type(got) != type(want):
            got_type = type(want).__name__
            if isinstance(want, FoldedScalarString):
                got_type = "folded string, indicated by |"
            if isinstance(want, LiteralScalarString):
                got_type = "literal string, indicated by >"
            raise KeyTypeError(key[1:], got_type)

        if isinstance(got, OrderedDict):
            got_keys = set(got.keys())
            want_keys = set(want.keys())

            unsupported_keys = got_keys - want_keys
            if unsupported_keys:
                raise UnsupportedKeyError([f"{key}.{k}"[1:] for k in unsupported_keys])

            not_found_keys = want_keys - got_keys
            if not_found_keys:
                raise NotFoundKeyError([f"{key}.{k}"[1:] for k in not_found_keys])

            for k in got.keys():
                self._validate(got[k], want[k], f"{key}.{k}")
        elif isinstance(got, list):
            want_item = want[0]
            for idx, got_item in enumerate(got):
                self._validate(got_item, want_item, f"{key}[{idx}]")
