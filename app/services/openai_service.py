from langchain_openai import ChatOpenAI

def get_llm():
    llm = ChatOpenAI(
    model="gpt-4o-mini", 
    temperature=0.7
    )
    return llm