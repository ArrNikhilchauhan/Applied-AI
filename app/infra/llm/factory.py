from app.core.config import setting
from app.infra.llm.base import BaseLLM
from app.infra.llm.dummy import DummyLLM
from app.core.exceptions import AppException
from app.infra.llm.registry import REGISTRY

def get_llm(provider:str)->BaseLLM:
    llm=REGISTRY.get(provider)
    if not llm:
        raise AppException("Invalid LLM Provider",500)
    return llm()
    
