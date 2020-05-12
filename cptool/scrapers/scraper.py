from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

from cptool.utils import errors


class Scraper:
    def __init__(self, url: str):
        data = self._retrieve_webpage(url)
        self._soup = BeautifulSoup(data, "html.parser")

    def soup(self):
        return self._soup

    def parse(self):
        raise NotImplementedError()

    def _retrieve_webpage(self, url):
        req = Request(url, headers={"Accept": "*/*", "User-Agent": "curl/7.58.0"},)
        data = urlopen(req).read()
        if not data:
            raise errors.CptoolError("fail to retrieve webpage.")

        return data
