import os

import sentry_sdk
from fastapi import FastAPI, Request
from fastapi.exceptions import HTTPException, RequestValidationError
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from httpx import NetworkError, TimeoutException
from pydantic import HttpUrl
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware

from .schemas import MetaResponseScheme
from .scraper import SiteScrapper

sentry_dsn = os.getenv("SENTRY_DSN", False)
if sentry_dsn:
    sentry_sdk.init(dsn=sentry_dsn, traces_sample_rate=1.0)


app = FastAPI()

if sentry_dsn:
    app.add_middleware(SentryAsgiMiddleware)

# fix nginx issues
app.add_middleware(ProxyHeadersMiddleware, trusted_hosts="*")
app.mount("/static", StaticFiles(directory="apimeta/static"), name="static")
templates = Jinja2Templates(directory="apimeta/templates")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(dict(detail="Url validation error"), status_code=400)


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", dict(request=request))


@app.get("/info")
async def info(url: HttpUrl) -> MetaResponseScheme:
    try:
        scrapper = SiteScrapper(url)
        tags = await scrapper.parse()
        return MetaResponseScheme.create(tags)
    except NetworkError:
        raise HTTPException(status_code=500, detail="Connection error")
    except TimeoutException:
        raise HTTPException(status_code=500, detail="Connection timeout")
    except RequestValidationError:
        raise HTTPException(status_code=500, detail="Validation error")
