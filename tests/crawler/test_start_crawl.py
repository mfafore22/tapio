import os 
from dotenv import load_dotenv
from tapio.crawler.client import start_crawl

load_dotenv()

ACCOUNT_ID = os.getenv("CLOUDFLARE_ACCOUNT_ID")
API_TOKEN = os.getenv("CLOUDFLARE_API_TOKEN")

def test_start_crawl_returns_job_id():
    job_id = start_crawl(ACCOUNT_ID, API_TOKEN, "https://example.com")

    assert job_id is not None
    assert isinstance(job_id, str)
    assert len(job_id) > 0