"""
Crawler module for migri-assitant.

Uses cloudflare / crawl API to fetch and parse web content

"""

from tapio.crawler.client import start_crawl, wait_for_crawl

__all__ = ["start_crawl", "wait_for_crawl"]