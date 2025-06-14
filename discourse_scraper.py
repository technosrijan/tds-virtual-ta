import requests
import time
from datetime import datetime
from bs4 import BeautifulSoup

BASE_URL = "https://discourse.onlinedegree.iitm.ac.in"
CATEGORY_PATH = "/c/courses/tds-kb/34"
CATEGORY_API_URL = f"{BASE_URL}{CATEGORY_PATH}.json"
TOPIC_API_URL = f"{BASE_URL}/t/{{}}.json"

# Paste the cookie values here from chrome dev tools (strings only, no quotes)
COOKIE_VALUES = {
    "_bypass_cache": "VALUE",        # e.g. "true"
    "_fbp": "VALUE",                 # e.g. "fb.2.1743320926329.140147020162572915"
    "_forum_session": "VALUE",       # e.g. "RZJfUFcFglYU3PI...etc"
    "_ga": "VALUE",                  # e.g. "GA1.1.1987251462.1743320927"
    "_ga_08NPRH5L4M": "VALUE",       # e.g. "GS1.1.1743328827.2.0.1743328827.60.0.0"
    "_gcl_au": "VALUE",              # e.g. "1.1.1720842340.1743320926"
    "_t": "VALUE",                   # e.g. "T0JtYU7RWnpTtJHs2aI6FczxvDB6tRkgMhfXdI9z..."
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": BASE_URL,
    # Cookie will be set via session.cookies below
}


def build_cookie_header(cookie_dict):
    return "; ".join([f"{k}={v}" for k, v in cookie_dict.items() if v])


session = requests.Session()
session.headers.update(HEADERS)
session.cookies.update(COOKIE_VALUES)  # this sets cookies from dict

def fetch_category_page(page):
    url = f"{CATEGORY_API_URL}?page={page}"
    resp = session.get(url)
    resp.raise_for_status()
    return resp.json()


def fetch_topic_details(topic_id):
    url = TOPIC_API_URL.format(topic_id)
    resp = session.get(url)
    resp.raise_for_status()
    return resp.json()


def parse_datetime(dt_str):
    return datetime.strptime(dt_str, "%Y-%m-%dT%H:%M:%S.%fZ")


def extract_post_text(post):
    return BeautifulSoup(post['cooked'], "html.parser").get_text()


def scrape_tds_kb(max_pages=5):
    all_posts = []
    START_DATE = datetime(2025, 1, 1)
    END_DATE = datetime(2025, 4, 14)

    for page in range(1, max_pages + 1):
        print(f"📄 Fetching page {page}...")
        category_data = fetch_category_page(page)
        for topic in category_data.get("topic_list", {}).get("topics", []):
            created_at = parse_datetime(topic['created_at'])
            if not (START_DATE <= created_at <= END_DATE):
                continue
            topic_id = topic["id"]
            slug = topic["slug"]
            print(f"🔍 Fetching topic {topic_id} - {slug}")
            topic_data = fetch_topic_details(topic_id)
            posts = [
                {
                    "post_number": post["post_number"],
                    "author": post["username"],
                    "content": extract_post_text(post)
                }
                for post in topic_data["post_stream"]["posts"]
            ]
            all_posts.append({
                "topic_id": topic_id,
                "title": topic["title"],
                "created_at": topic["created_at"],
                "url": f"{BASE_URL}/t/{slug}/{topic_id}",
                "posts": posts
            })
        time.sleep(1)
    return all_posts


if __name__ == "__main__":
    import json
    result = scrape_tds_kb(max_pages=10)
    with open("tds_kb_scraped.json", "w") as f:
        json.dump(result, f, indent=2)
    print(f"✅ Saved {len(result)} topics to tds_kb_scraped.json")