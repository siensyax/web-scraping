import asyncio
import urllib.request
from bs4 import BeautifulSoup


class Scraping:
    def __init__(self, urls):
        self.urls = urls

    def run(self):
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(self.fetch())

    async def fetch(self):
        return await asyncio.wait(
            [self.scraping(url) for url in self.urls]
        )

    async def scraping(self, url):
        request = urllib.request.Request(url)
        html = urllib.request.urlopen(request).read()
        bs = BeautifulSoup(html, "html.parser")
        print(bs.title.string)


if __name__ == "__main__":
    scraping = Scraping([
        "https://www.python.org/", 
        "https://www.python.org/about/", 
        "https://www.python.org/downloads/"
    ])

    scraping.run()
