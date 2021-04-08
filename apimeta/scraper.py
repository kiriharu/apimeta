from typing import List

from bs4 import BeautifulSoup
from httpx import AsyncClient, Response

from apimeta.tags import DefaultTagType, MetaTag, tag_factory


class SiteScrapper:

    def __init__(self, url: str):
        self.url = url

    async def _request(self) -> str:
        async with AsyncClient() as client:
            resp: Response = await client.get(self.url)
        return resp.text

    async def _get_soup(self) -> BeautifulSoup:
        content = await self._request()
        return BeautifulSoup(content)

    async def parse(self) -> List[DefaultTagType]:
        soup = await self._get_soup()
        head = soup.find("head")
        meta_list = head.find_all("meta")
        tags = [tag_factory(MetaTag(meta)) for meta in meta_list]
        return tags
