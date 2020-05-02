import sys
from pathlib import Path

from cptool.utils import console_io as io
from cptool.utils import errors
from cptool.yaml import YamlFile

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
input: |
output: |
constraints: >
examples:
  - input: |
    output: |
    explanation: >
"""


class ProblemYamlGenerator:
    def __init__(self, problem_name: str):
        self._problem_name = problem_name
        self._yaml = YamlFile()
        self._yaml.load(YAML_DEFAULT)
        self._content = self._yaml.content

    def generate(self, yaml_file: Path):
        if io.confirm(
            "Would you like to scrap problem information from URL?\n"
            "  Supporting sites: CodeChef.\n"
            "  (yes/no) [yes] ",
            default=True,
        ):
            self._scraping()
        else:
            self._manual()

        io.line("Generated file")
        io.line()
        self._yaml.dump(stream=sys.stdout)
        io.line()

        if not io.confirm("Do you confirm generation? (yes/no) [yes] ", default=True):
            raise errors.CptoolError("command aborted.")

        self._yaml.dump(stream=yaml_file)

    def _manual(self):
        name = io.ask(
            "Problem name [{}]: ".format(self._problem_name), default=self._problem_name
        )

        code = io.ask("Problem code []: ", default="")

        url = io.ask("Problem URL []: ", default="")

        self._content["name"] = name
        self._content["code"] = code
        self._content["url"] = url

    def _scraping(self):
        pass
