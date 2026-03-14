from app.services.openai_service import get_llm

def report_agent(state):

    llm = get_llm()

    analysis = state["analysis"]

    prompt = f"Generate a research report from this analysis:\n{analysis}"

    response = llm.invoke(prompt)

    return {"final_report": response.content}