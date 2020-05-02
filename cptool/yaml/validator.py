from collections import OrderedDict
from pathlib import Path
from typing import List, Union

from ruamel.yaml.scalarstring import FoldedScalarString, LiteralScalarString

from cptool.utils import YamlFile
from cptool.utils.errors import KeyTypeError, NotFoundKey, UnsupportedKey
from cptool.yaml.default import YAML_DEFAULT


class ProblemYamlValidator:
    def __init__(self, problem_yaml_default=YAML_DEFAULT):
        self._expected = YamlFile().load(problem_yaml_default)

    def validate(self, problem_yaml: Union[Path, OrderedDict, str]):
        content = (
            problem_yaml
            if isinstance(problem_yaml, OrderedDict)
            else YamlFile().load(problem_yaml)
        )

        unsupported_keys, not_found_keys = self._validate_keys(content, self._expected)

        if unsupported_keys:
            raise UnsupportedKey(unsupported_keys)
        if not_found_keys:
            raise NotFoundKey(not_found_keys)

        self._validate_types(content, self._expected)

    def _validate_keys(self, got: OrderedDict, want: OrderedDict):
        if not isinstance(got, OrderedDict):
            return [[], want.keys()]

        unsupported_keys: List[str] = []
        not_found_keys: List[str] = []

        got_keys = set(got.keys())
        want_keys = set(want.keys())

        unsupported_keys += got_keys - want_keys
        not_found_keys += want_keys - got_keys

        for want_key in want_keys.intersection(got_keys):
            unsupported = []
            not_found = []
            if isinstance(want[want_key], OrderedDict):
                unsupported, not_found = self._validate_keys(
                    got.get(want_key, {}), want[want_key]
                )
            elif isinstance(got[want_key], list) and isinstance(want[want_key], list):
                elem_want = want[want_key][0]
                if isinstance(elem_want, OrderedDict):
                    for elem_got in got[want_key]:
                        unsupported, not_found = self._validate_keys(
                            elem_got, elem_want
                        )
            unsupported_keys += [f"{want_key}.{k}" for k in unsupported]
            not_found_keys += [f"{want_key}.{k}" for k in not_found]

        return [unsupported_keys, not_found_keys]

    def _validate_types(self, got: OrderedDict, want: OrderedDict):
        for key, value in want.items():
            if type(got[key]) != type(value):
                if isinstance(value, FoldedScalarString):
                    raise KeyTypeError(key, "folded string, indicated by >")
                elif isinstance(value, LiteralScalarString):
                    raise KeyTypeError(key, "literal string, indicated by |")
                elif isinstance(value, str):
                    raise KeyTypeError(key, "string")
                elif isinstance(value, list):
                    raise KeyTypeError(key, "list")
                else:
                    raise KeyTypeError(key, str(type(value)))
            else:
                if isinstance(want[key], OrderedDict):
                    self._validate_types(got[key], want[key])
