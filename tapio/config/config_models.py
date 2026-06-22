"""Configuration models for HTML content parsers.

This module contains Pydantic models that define the configuration for
site-specific HTML parsing, including content selectors and HTML-to-Markdown
conversion settings.
"""

from typing import Annotated, Literal
from urllib.parse import urlparse

from pydantic import BaseModel, Field, HttpUrl


class CrawlerConfig(BaseModel):
    max_depth : Annotated[int, Field(ge=1, le=10)] = 2
    limit : Annotated[int, Field(ge=1, le=100_000)] = 100
    render: bool = True
    source: Literal["all", "sitemaps", "links"] = "all"


class SiteConfig(BaseModel):
    base_url : HttpUrl
    description: str | None = None
    crawler_config: CrawlerConfig = Field(default_factory=CrawlerConfig)


    @property
    def base_dir(self) -> str:
        url_str = str(self.base_url)
        parsed = urlparse(url_str)
        host = parsed.hostname
        if not host:
            raise ValueError(f"invalid base_url: {url_str}")
        return host


class ParserConfigRegistry(BaseModel):
    sites: dict[str, SiteConfig]


