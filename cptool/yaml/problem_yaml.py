from collections import OrderedDict
from pathlib import Path

from ruamel.yaml.scalarstring import FoldedScalarString, LiteralScalarString

from cptool.utils import YamlFile

YAML_DEFAULT = u"""\
name: ''
code: ''
url: ''
metadata:
  # beginner, easy, medium, hard, challenge
  level: ''
  tags: ''
  contest:
    name: ''
    url: ''
    code: ''
statement: >
input: >
output: >
constraints: >
examples:
  - input: |
    output: |
    explanation: >
"""


class ProblemYaml:
    def __init__(self):
        self._content = None

    @property
    def name(self):
        pass

    @name.setter
    def name(self, problem_name):
        pass

    @property
    def code(self):
        pass

    @code.setter
    def code(self, problem_code):
        pass

    def validate(self, file: Path):
        pass

    def read(self, file: Path):

        pass

    def save(self, file: Path):
        pass

    def _validate(self, data: OrderedDict):
        pass

    def _validate_name(self, name):
        pass

    def _validate_code(self, code):
        pass

    def _validate_input(self, input):
        pass

    def _validate_output(self, output):
        pass
