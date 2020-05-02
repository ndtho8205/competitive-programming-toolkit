import re
from collections import OrderedDict
from pathlib import Path
from typing import List, Union

from ruamel.yaml.scalarstring import FoldedScalarString, LiteralScalarString

from cptool.utils import YamlFile
from cptool.utils.errors import KeyTypeError, NotFoundKey, UnsupportedKey
from cptool.yaml.problem_yaml import YAML_DEFAULT


class ProblemYamlValidator:
    PATTERN_NAME = r"[a-zA-Z]+[0-9]+"

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

        for key in want_keys.intersection(got_keys):
            if isinstance(want[key], OrderedDict):
                unsupported, not_found = self._validate_keys(
                    got.get(key, {}), want[key]
                )
                unsupported_keys += [f"{key}.{k}" for k in unsupported]
                not_found_keys += [f"{key}.{k}" for k in not_found]
            elif isinstance(want[key], list):
                # TODO: implement validate a list of  examples
                pass

        return [unsupported_keys, not_found_keys]

    def _validate_types(self, got: OrderedDict, want: OrderedDict):
        for key, value in want.items():
            if type(got[key]) != type(value):
                print(key, isinstance(value, FoldedScalarString))
                if isinstance(value, FoldedScalarString):
                    raise KeyTypeError(key, "folded string, indicated by >")
                elif isinstance(value, LiteralScalarString):
                    raise KeyTypeError(key, "literal style, indicated by |")
                elif type(value) == type(str):
                    raise KeyTypeError(key, "string")
                elif isinstance(value, list):
                    # TODO: implement validate type of example list
                    pass
            if isinstance(want[key], OrderedDict):
                self._validate_types(got[key], want[key])
