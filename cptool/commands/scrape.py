from cptool.scrapers.scraper import Scraper


class ScrapeCommand:
    """Scrape problem url."""

    def __call__(self, args):
        self.handle(args.url)

    def register_arguments(self, parser):
        parser.add_argument(
            "url", metavar="<path>", type=str, help="problem url",
        )

    def handle(self, url: str = ""):
        url = "https://www.codechef.com/LRNDSA02/problems/STFOOD"
        scraper = Scraper()
        scraper.scrape(url)
        print("Successfully scraped problem.")
