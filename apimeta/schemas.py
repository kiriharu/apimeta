from typing import List

from pydantic import BaseModel, Field
from .tags import (
    TwitterTag, OpenGraphTag, DefaultTag, TitleTag
)


class AppsScheme(BaseModel):
    twitter: List[TwitterTag] = Field(default=[])

    class Config:
        arbitrary_types_allowed = True


class MetaResponseScheme(BaseModel):
    title: List[TitleTag] = Field(default=None)
    opengraph: List[OpenGraphTag] = Field(default=[])
    apps: AppsScheme = Field(default={})
    tags: List[DefaultTag] = Field(default=[])

    class Config:
        arbitrary_types_allowed = True

    @classmethod
    def create(cls, tags: List[DefaultTag]):

        tag_types = {
            TitleTag: [], TwitterTag: [],
            OpenGraphTag: [], DefaultTag: [],
        }

        for tag in tags:
            tag_types.get(type(tag), []).append(tag)

        return cls(
            title=tag_types[TitleTag],
            opengraph=tag_types[OpenGraphTag],
            tags=tag_types[DefaultTag],
            apps=AppsScheme(twitter=tag_types[TwitterTag])
        )
