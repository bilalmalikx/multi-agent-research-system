from app.tools.web_search import web_search

def research_agent(state):
    query = state["query"]
    search_results = web_search(query)  
    return {"search_results": search_results}