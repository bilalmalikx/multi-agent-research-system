import requests
from bs4 import BeautifulSoup

def scrape_web_page(url):
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        paragraphs = soup.find_all('p')
        text = [p.get_text() for p in paragraphs]

        return text
    except Exception as e:
        return [f"Error scraping {url}: {str(e)}"]