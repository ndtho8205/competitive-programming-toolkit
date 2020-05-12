from cptool.scrapers.scraper import Scraper


class CodeChefScraper(Scraper):
    def parse_problem_name(self):
        return self._soup.h1.contents[0].strip()

    def parse_problem_code(self):
        return self._soup.find(id="problem-code").string.strip()

    def parse_metadata_level(self):
        second_level = self._soup.find(class_="breadcrumb").find_all("a")[1]
        if second_level["href"].startswith("/problems/"):
            return second_level["href"].split("/")[2]
        return ""

    def parse_metadata_tags(self):
        pass

    def parse_metadata_contest(self):
        breadcrumbs = self._soup.find(class_="breadcrumb").find_all("a")
        second_level = breadcrumbs[1]
        if second_level["href"] != "/contests/":
            return ""

        third_level = breadcrumbs[2]

        name = third_level.string.strip()
        code = third_level["href"].replace("/", "")
        url = f"https://www.codechef.com/{code}"

        return name, code, url

    def parse_statement(self):
        pass

    def parse_input(self):
        input = self._soup.find_all("h3", text="Example")
        if not input:
            return ""
        p = input[0].find_next_sibling()
        return p.text.strip()

    def parse_output(self):
        pass

    def parse_constraints(self):
        pass

    def parse_example(self):
        example = self._soup.find_all("h3", text="Example")
        if not example:
            return None

        pre = example[0].find_next_sibling()
        b = pre.find_all("b")

        input = b[0].find_next_sibling(string=True).strip()
        output = b[1].find_next_sibling(string=True).strip()
        explanation = ""

        return input, output, explanation
