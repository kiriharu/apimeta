from fastapi import FastAPI
from .schemas import MetaResponseScheme
from .scraper import SiteScrapper

app = FastAPI()


@app.get("/info")
async def info(url: str) -> MetaResponseScheme:
    scrapper = SiteScrapper(url)
    tags = await scrapper.parse()
    return MetaResponseScheme.create(tags)

