from app.infra.llm.base import BaseLLM
from app.core.exceptions import AppException

class LLMService:
    def __init__(self,llm:BaseLLM):
        self.llm=llm

    def run(self,prompt:str):
        try:
            return self.llm.generate(prompt)
        except Exception:
            raise AppException("LLM Failed due to any reason",500)


