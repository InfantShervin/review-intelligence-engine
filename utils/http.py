import requests
from tenacity import retry, stop_after_attempt, wait_exponential

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

@retry(stop=stop_after_attempt(2), wait=wait_exponential(multiplier=1, min=2, max=6))
def fetch(url: str):
    """
    Fetch page HTML using requests.
    Returns None if access is forbidden (403).
    """
    response = requests.get(url, headers=HEADERS, timeout=10)

    # IMPORTANT: Do not crash on protected pages
    if response.status_code == 403:
        return None

    response.raise_for_status()
    return response.text

