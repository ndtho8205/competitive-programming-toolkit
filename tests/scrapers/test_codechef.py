from cptool.scrapers import Scraper


class CodeChefScraper(Scraper):
    def _parse_problem_name(self):
        return self._soup.h1.contents[0].strip()

    def _parse_problem_code(self):
        return self._soup.find(id="problem-code").string.strip()

    def _parse_metadata_level(self):
        pass

    def _parse_metadata_tags(self):
        pass

    def _parse_metadata_contest_name(self):
        pass

    def _parse_metadata_contest_url(self):
        pass

    def _parse_metadata_contest_code(self):
        pass

    def _parse_statement(self):
        pass

    def _parse_input(self):
        pass

    def _parse_output(self):
        pass

    def _parse_constraints(self):
        pass

    def _parse_examples(self):
        pass

    def _parse_example_input(self):
        pass

    def _parse_example_output(self):
        pass

    def _parse_example_explanation(self):
        pass
