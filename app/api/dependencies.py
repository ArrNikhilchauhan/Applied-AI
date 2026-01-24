from app.services.llm_service import LLMService
from app.services.system_service import SystemService
from app.infra.llm.factory import get_llm
from app.core.config import setting

def get_llm_service()->LLMService:
    return LLMService(get_llm(setting.LLM_PROVIDER))

def get_system_service()->SystemService:
    return SystemService()      