from bs4.element import Tag
from typing import Optional

from apimeta.utils import without_keys


class MetaTag:

    def __init__(self, tag: Tag):
        self.name: Optional[str] = tag.get("name", None)
        self.content: Optional[str] = tag.get("content", None)
        self.property: Optional[str] = tag.get("property", None)
        self.other: Optional[dict] = without_keys(
            tag.attrs, {"name", "content", "property"}
        )

    def name_contain(self, name: str) -> bool:
        """Returns true if tag contains provided name"""
        return isinstance(self.name, str) and name in self.name

    def name_eq(self, name: str) -> bool:
        return isinstance(self.name, str) and name == self.name

    def property_eq(self, property_: str) -> bool:
        return isinstance(self.property, str) and property_ == self.property

    def property_contain(self, property_: str) -> bool:
        """Returns true if tag contains provided property"""
        return isinstance(self.property, str) and property_ in self.property


# TODO: abstracttagtype
class DefaultTagType:
    """Default Tag type"""

    def __init__(self, tag: MetaTag):
        self.tag = tag

    @property
    def __dict__(self):
        return self.tag

    @classmethod
    def check(cls, tag: MetaTag) -> bool:
        raise NotImplementedError


class TitleTag(DefaultTagType):

    @classmethod
    def check(cls, tag: MetaTag) -> bool:
        return tag.name_eq("title")


class TwitterTag(DefaultTagType):

    @classmethod
    def check(cls, tag: MetaTag) -> bool:
        return tag.name_contain("twitter")


class OpenGraphTag(DefaultTagType):

    @classmethod
    def check(cls, tag: MetaTag) -> bool:
        return tag.property_contain("og") or tag.name_contain("og")


def tag_factory(meta_tag: MetaTag):
    for cls in DefaultTagType.__subclasses__():
        if cls.check(meta_tag):
            return cls(meta_tag)
    else:
        return DefaultTagType(meta_tag)
