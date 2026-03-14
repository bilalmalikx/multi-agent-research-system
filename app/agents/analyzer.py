from app.services.openai_service import get_llm

def analyzer_agent(state):

    llm = get_llm()

    text = "\n".join(state["scraped_data"])

    prompt = f"Analyze this data:\n{text}"

    response = llm.invoke(prompt)

    return {"analysis": response.content}