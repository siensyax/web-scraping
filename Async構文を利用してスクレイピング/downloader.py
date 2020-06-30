import asyncio
import urllib.request


class Downloader:
    def __init__(self, urls):
        self.urls = urls

    def run(self):
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(self.fetch())

    async def fetch(self):
        return await asyncio.wait(
                [self.download(i, url) for i, url in enumerate(self.urls)]
                )

    async def download(self, n, url):
        request = urllib.request.Request(url)
        html = urllib.request.urlopen(request).read()
        print("{0} {1} download finish...".format(n, url))
        return html


if __name__ == "__main__":
    downloader = Downloader([
        "https://www.python.org/",
        "https://www.python.org/about/",
        "https://www.python.org/downloads/"
    ])

    downloader.run()
