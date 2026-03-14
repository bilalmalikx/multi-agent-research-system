from langgraph.graph import StateGraph
from app.state import ResearchAgentState

from app.agents.researcher import research_agent
from app.agents.scraper import scraper_agent
from app.agents.analyzer import analyzer_agent
from app.agents.report_generator import report_agent


builder = StateGraph(ResearchAgentState)

builder.add_node("research", research_agent)
builder.add_node("scrape", scraper_agent)
builder.add_node("analyze", analyzer_agent)
builder.add_node("report", report_agent)

builder.set_entry_point("research")

builder.add_edge("research", "scrape")
builder.add_edge("scrape", "analyze")
builder.add_edge("analyze", "report")

graph = builder.compile()