import os
from urllib.parse import urlparse
from datetime import datetime, timezone
from tapio.crawler.client import start_crawl, wait_for_crawl

class CrawlerRunner:
    def __init__(self, account_id: str, api_token: str , output_base_dir: str = "content"):
       self.account_id = account_id
       self.api_token = api_token
       self.output_base_dir = output_base_dir

    def run(self , site_name , url: str) -> int:

        print(f"Starting crawl for {site_name} at {url}")

        job_id = start_crawl(self.account_id, self.api_token, url)
        print(f" Job started: {job_id}")

        result = wait_for_crawl(self.account_id, job_id, self.api_token)
        records = result.get("records", [])

        print(f"Got {len(records)} records")

        saved_count = 0
        for record in records:
            if record.get("status") != "completed":
                continue
            self._save_record(site_name, record)
            saved_count += 1
        
        print(f"Saved {saved_count} files")
        return saved_count
    
    def _save_record(self , site_name: str , record: dict):
       output_dir = os.path.join(self.output_base_dir, site_name, "parsed")
       os.makedirs(output_dir, exist_ok=True)

       filepath = os.path.join(output_dir, f"{self._url_to_filename(record['url'])}.md")
       content = self._build_frontmatter(record) + record.get("markdown", "")

       with open(filepath, "w", encoding="utf-8") as f:
           f.write(content)
    
    def _url_to_filename(self, url) -> str:
        path = urlparse(url).path.strip("/")

        if not path:
            return "index"
        
        return path.replace("/", "-").lower()
    
    def _build_frontmatter(self , record:dict) -> str:
        title = record.get("metadata",  {}).get("title", "Untitled")
        source_url = record["url"]
        timestamp = datetime.now(timezone.utc).isoformat()

        return f""" 
title: "{title}"
source_url: "{source_url}"
crawl_timestamp: "{timestamp}"
"""