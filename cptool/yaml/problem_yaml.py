import copy
from pathlib import Path
from typing import Union

from ruamel.yaml.comments import CommentedMap
from ruamel.yaml.scalarstring import FoldedScalarString, LiteralScalarString

from cptool.utils import YamlFile
from cptool.yaml.default import YAML_DEFAULT
from cptool.yaml.validator import ProblemYamlValidator


class ProblemYaml:
    def __init__(self, problem_yaml: Union[str, Path] = None):
        self._yaml = YamlFile()

        if problem_yaml:
            if ProblemYamlValidator().validate(problem_yaml):
                self._content = self._yaml.load(problem_yaml)
        else:
            self._content = self._yaml.load(YAML_DEFAULT)
            self._content["examples"] = []

    @property
    def content(self):
        return copy.deepcopy(self._content)

    def set_basic_info(self, name: str = "", code: str = "", url: str = ""):
        self._content["name"] = name
        self._content["code"] = code
        self._content["url"] = url

    def set_metadata(
        self,
        level: str = "",
        tags: str = "",
        contest_name: str = "",
        contest_url: str = "",
        contest_code: str = "",
    ):
        self._content["metadata"]["level"] = level
        self._content["metadata"]["tags"] = tags
        self._content["metadata"]["contest"]["name"] = contest_name
        self._content["metadata"]["contest"]["code"] = contest_code
        self._content["metadata"]["contest"]["url"] = contest_url

    def set_statement(self, statement: str, input: str, output: str, constraints: str):
        self._content["statement"] = FoldedScalarString(statement)
        self._content["input"] = FoldedScalarString(input)
        self._content["output"] = FoldedScalarString(output)
        self._content["constraints"] = FoldedScalarString(constraints)

    def add_examples(self, input: str, output: str, explanation: str):
        example = CommentedMap(
            input=LiteralScalarString(input),
            output=LiteralScalarString(output),
            explanation=FoldedScalarString(explanation),
        )
        self._content["examples"].append(example)

    def __str__(self):
        return self._yaml.dump(self._content, None)

    def save(self, path: Path):
        return self._yaml.dump(self._content, path)

    def export(self, stream=None, format="markdown"):
        raise NotImplementedError()
