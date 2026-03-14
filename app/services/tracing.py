import os 


def tracing_llm():
    os.environ['LANGSMITH_TRACING_V2'] = 'true'