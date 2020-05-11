from cptool.scrapers.codechef import CodeChefScraper
from cptool.scrapers.scraper import Scraper


def get_scraper(url: str):
    if url.find("codechef.com"):
        return CodeChefScraper()


__all__ = ["Scraper", "CodeChefScraper", "get_scraper"]
