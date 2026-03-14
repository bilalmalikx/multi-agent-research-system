from app.tools.scraper_tool import scrape_web_page

def scraper_agent(state):

    urls = state["search_results"]

    data = []

    for url in urls:

        data.extend(scrape_web_page(url))

    return {"scraped_data": data}