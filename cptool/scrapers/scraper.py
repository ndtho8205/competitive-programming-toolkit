from pathlib import Path
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

from cptool.utils import errors


class Scraper:
    def __init__(self):
        self._soup = ""

    def soup(self):
        return self._soup

    def scrap(self, url):
        data = self._retrieve_webpage(url)
        with Path("/home/ndtho8205/Desktop/retrieve.html").open("w") as f:
            f.write(data.decode())
        self._soup = BeautifulSoup(data, "html.parser")

    def parse(self):
        raise NotImplementedError()

    def _retrieve_webpage(self, url):
        req = Request(url, headers={"Accept": "*/*", "User-Agent": "curl/7.58.0"},)
        data = urlopen(req).read()
        if not data:
            raise errors.CptoolError("fail to retrieve webpage.")

        return data
