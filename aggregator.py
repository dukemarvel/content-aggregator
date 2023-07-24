import feedparser
from bs4 import BeautifulSoup



FEED_URLS = [
    'http://feeds.bbci.co.uk/news/world/rss.xml',
    'https://www.theguardian.com/world/rss',
    'https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml',
    'http://feeds.feedburner.com/NasaBreakingNews',
]

def clean_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.get_text()

def fetch_entries(feed_urls, limit=None):
    all_entries = []
    for url in feed_urls:
        feed = feedparser.parse(url)
        entries = feed.entries[:limit] if limit else feed.entries
        for entry in entries:
            clean_title = clean_html(entry.title)
            transformed_entry = {
                'title': clean_title,
                'link': entry.link,
                'published': entry.published,
                'source': feed.feed.title,
            }
            all_entries.append(transformed_entry)
    return all_entries






