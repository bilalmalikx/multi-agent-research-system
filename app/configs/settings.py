from pydentic import BaseModel

class Settings(BaseModel):
    OPENAI_API_KEY: str
    LANGSMITH_API_KEY: str
    LANGSMITH_PROJECT: str

    class config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()