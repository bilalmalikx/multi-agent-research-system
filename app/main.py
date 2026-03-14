from fastapi import FastAPI
from app.graph import graph

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Research Agent Running"}


@app.post("/research")

def run_research(query: str):

    result = graph.invoke(
        {
            "query": query,
            "search_results": [],
            "scraped_data": [],
            "analysis": "",
            "final_report": ""
        }
    )

    return result