from cptool.utils import console_io as io
from cptool.utils import errors
from cptool.yaml import ProblemYaml


class ProblemYamlGenerator:
    def __init__(self, problem_name: str):
        self._problem_name = problem_name
        self._yaml = ProblemYaml()

    def generate(self):
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
        print(self._yaml.export())
        io.line()

        if not io.confirm("Do you confirm generation? (yes/no) [yes] ", default=True):
            raise errors.CptoolError("command aborted.")
        return self._yaml

    def _manual(self):
        name = io.ask(
            "Problem name [{}]: ".format(self._problem_name), default=self._problem_name
        )

        code = io.ask("Problem code []: ", default="")

        url = io.ask("Problem URL []: ", default="")

        self._yaml.set_basic_info(name, code, url)

    def _scraping(self):
        pass
