from cptool.scrapers import CodeChefScraper


class ScrapeCommand:
    """Scrape problem url."""

    def __call__(self, args):
        self.handle(args.url)

    def register_arguments(self, parser):
        parser.add_argument(
            "url", metavar="<path>", type=str, help="problem url",
        )

    def handle(self, url: str = ""):
        scraper = CodeChefScraper(url)
        print("Problem name:", scraper.parse_problem_name())
        print("Problem code:", scraper.parse_problem_code())
        print("Level:", scraper.parse_metadata_level())
        print("Contest:", scraper.parse_metadata_contest())
        print("Example:", scraper.parse_example())
