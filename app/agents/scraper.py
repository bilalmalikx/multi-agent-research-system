from app.tools.scraper_tool import scrape_url

def scraper_agent(state):

    urls = state["search_results"]

    data = []

    for url in urls:

        data.extend(scrape_url(url))

    return {"scraped_data": data}