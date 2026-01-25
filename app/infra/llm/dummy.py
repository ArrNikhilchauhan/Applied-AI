from app.infra.llm.base import BaseLLM
from app.core.exceptions import AppException

class DummyLLM(BaseLLM):
    def generate(self, prompt:str)->str:
        if prompt==None:
            raise AppException("No Prompt",500)
        return f"LLM Response :{prompt}"