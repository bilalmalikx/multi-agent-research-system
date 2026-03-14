import requests 

def web_search(query):
    url = url = f"https://duckduckgo.com/?q={query}"
    return [url]