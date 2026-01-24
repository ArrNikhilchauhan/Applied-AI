from app.infra.llm.base import BaseLLM

class DummyLLM(BaseLLM):
    def generate(self, prompt)->str:
        return f"LLM Response :{prompt}"