from typing import TypedDict, List 

class ResearchAgentState(TypedDict):
    query: str
    search_results: List[str]
    scraped_data: List[str]
    analysis: str
    final_report: str