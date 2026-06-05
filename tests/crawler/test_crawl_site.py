import os 
from dotenv import load_dotenv
from tapio.crawler.client import crawl_site


load_dotenv()

ACCOUNT_ID = os.getenv("CLOUDFLARE_ACCOUNT_ID")
API_TOKEN = os.getenv("CLOUDFLARE_API_TOKEN")

def test_crawl_site_returns_full_result():
    result = crawl_site(ACCOUNT_ID, API_TOKEN, "https://example.com")

    assert result is not None
    assert "status" in result
    assert "records" in result
    assert result["status"] != "running"


