import os
from dotenv import load_dotenv
from tapio.crawler.client import start_crawl, wait_for_crawl


load_dotenv()

ACCOUNT_ID = os.getenv("CLOUDFLARE_ACCOUNT_ID")
API_TOKEN = os.getenv("CLOUDFLARE_API_TOKEN")

def test_wait_for_crawl_returns_result():
    job_id = start_crawl(ACCOUNT_ID, API_TOKEN, "https://example.com")

    result = wait_for_crawl(ACCOUNT_ID, job_id, API_TOKEN)

    assert result is not None
    assert "status" in result
    assert result["status"] != "running"