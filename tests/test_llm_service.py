from app.services.llm_service import LLMService

class fake_llm():
    def generate(self,prompt:str):
        return "LLM"
    
def test_llm_service():
    service=LLMService(fake_llm())
    result=service.run("chla de bhai")
    assert result=="LLM"