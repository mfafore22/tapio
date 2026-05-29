import httpx
import time
def start_crawl(account_id: str, api_token: str, url: str) -> str:
    endpoint = f"https://api.com/client/v4/accounts/{account_id}/browser-rendering/crawl"

    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
    }

    payload = {
        "url": url,
    }

    response = httpx.post(endpoint, json=payload, headers = headers)
    response.raise_for_status
    data = response.json()
    job_id = data["result"]

    return job_id


def wait_for_crawl(account_id: str , job_Id: str, api_token: str) -> dict:
    max_Attempts = 60
    delay_ms = 5000

    for i in range(max_Attempts):
        url = f"https://api.com/client/v4/accounts/{account_id}/browser-rendering/crawl"
       
        headers = {
            "Authorization": f"Bearer {api_token}",

        }

        response = httpx.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        status = data["result"]["status"]

        if status != "running":
            return data["result"]
        
        time.sleep(delay_ms / 1000)

    raise TimeoutError("Crawl job did not  complete wiithin timeout")


def crawl_site(account_id:str, api_token: str, url: str) -> dict:

    job_id = start_crawl(account_id, api_token, url)

    result = wait_for_crawl(account_id, job_id, api_token)



