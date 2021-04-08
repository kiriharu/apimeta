from fastapi import FastAPI
from .schemas import MetaResponse
from .scraper import SiteScrapper

app = FastAPI()


@app.get("/info")
async def info(url: str) -> MetaResponse:
    scrapper = SiteScrapper(url)
    tags = await scrapper.parse()
    return MetaResponse.create(tags)

