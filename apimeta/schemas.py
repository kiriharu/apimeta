from typing import List

from pydantic import BaseModel, Field
from .tags import (
    TwitterTag, OpenGraphTag, DefaultTagType, TitleTag, MetaTag
)


class MetaResponse(BaseModel):
    title: List[TitleTag] = Field(default=None)
    opengraph: List[OpenGraphTag] = Field(default=[])
    twitter: List[TwitterTag] = Field(default=[])
    tags: List[DefaultTagType] = Field(default=[])

    class Config:
        arbitrary_types_allowed = True

    @classmethod
    def create(cls, tags: List[MetaTag]):

        tag_types = {
            TitleTag: [], TwitterTag: [],
            OpenGraphTag: [], DefaultTagType: [],
        }

        for tag in tags:
            tag_types.get(type(tag), []).append(tag)

        return cls(
            title=tag_types[TitleTag],
            twitter=tag_types[TwitterTag],
            opengraph=tag_types[OpenGraphTag],
            tags=tag_types[DefaultTagType]
        )
