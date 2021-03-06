from pathlib import Path

from cptool.scrapers import CodeChefScraper
from cptool.utils import console_io as io
from cptool.utils import errors
from cptool.yaml import ProblemYaml

TEST_CASE_GENERATOR_DEFAULT = """\
from typing import Callable

# MIN_N = 1
# MAX_N = 1000000


def generate(f_rand: Callable[[int, int], int]):
    # f_rand(min_range, max_range) is a function
    # that return a pesudo-random integer
    # in [min_range, max_range]
    # print(f_rand(MIN_N, MAX_N))
    raise NotImplementedError()


if __name__ == "__main__":
    generate(f_rand=lambda x, y: 3)
"""


class Template:
    def __init__(self, interactive: bool):
        self._interactive = interactive

    def create(self, problem_dir: Path):
        problem_dir.mkdir(parents=True, exist_ok=True)

        self.create_structure(problem_dir)
        self.create_test_cases_generator(problem_dir)
        self.create_problem_yaml(problem_dir)
        self.create_readme(problem_dir)

    def create_structure(self, problem_dir: Path):
        code_dir = problem_dir / "codes"
        code_dir.mkdir(parents=True, exist_ok=True)

        test_cases_dir = problem_dir / "test_cases"
        test_cases = ["generated", "handmade", "examples"]
        for test in test_cases:
            (test_cases_dir / test).mkdir(parents=True, exist_ok=True)

    def create_test_cases_generator(self, problem_dir: Path):
        test_case_generator_file = problem_dir / "test_cases" / "generator.py"
        test_case_generator_file.parent.mkdir(parents=True, exist_ok=True)
        test_case_generator_file.write_text(TEST_CASE_GENERATOR_DEFAULT, "utf-8")

    def create_problem_yaml(self, problem_dir: Path):
        problem_dir.mkdir(parents=True, exist_ok=True)
        problem_name = problem_dir.name

        self._problem_yaml = ProblemYaml()

        if not self._interactive:
            self._problem_yaml.set_basic_info(problem_name)
        else:
            if io.confirm(
                "Would you like to automatically extract problem information from URL?\n"
                "  Supporting sites: CodeChef.\n"
                "  (yes/no) [yes] ",
                default=True,
            ):
                self._scrape()
            else:
                self._manual(problem_name)

            io.line("Generated file")
            io.line()
            print(self._problem_yaml)
            io.line()

            if not io.confirm(
                "Do you confirm generation? (yes/no) [yes] ", default=True
            ):
                raise errors.CptoolError("command aborted.")

        self._problem_yaml.save(problem_dir / "problem.yaml")

    def create_readme(self, problem_dir: Path):
        readme_file = problem_dir / "README.md"
        readme_file.touch()

    def _manual(self, problem_name: str = ""):
        name = io.ask(f"Problem name [{problem_name}]: ", default=problem_name)

        code = io.ask("Problem code []: ", default="")

        url = io.ask("Problem URL []: ", default="")

        self._problem_yaml.set_basic_info(name, code, url)

    def _scrape(self):
        url = io.ask("Problem URL: ", default="")
        if "codechef.com" in url:
            scraper = CodeChefScraper(url)
        else:
            raise errors.CptoolError("website is not supported.")

        name = scraper.parse_problem_name()
        code = scraper.parse_problem_code()
        self._problem_yaml.set_basic_info(name, code, url)

        level = scraper.parse_metadata_level()
        tags = scraper.parse_metadata_tags()
        (contest_name, contest_code, contest_url) = scraper.parse_metadata_contest()
        self._problem_yaml.set_metadata(
            level, tags, contest_name, contest_url, contest_code
        )

        statement = scraper.parse_statement()
        input = scraper.parse_input()
        output = scraper.parse_output()
        constraints = scraper.parse_constraints()
        self._problem_yaml.set_statement(statement, input, output, constraints)

        example_input, example_output, example_explanation = scraper.parse_example()
        self._problem_yaml.add_examples(
            example_input, example_output, example_explanation
        )
