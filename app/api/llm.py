from fastapi import APIRouter,Depends
from app.schemas.ai import PromptRequest
from app.api.dependencies import get_llm_service

llm_router=APIRouter()

@llm_router.post('/prompt')
def prompt(query:PromptRequest,service=Depends(get_llm_service)):
    return {"response":service.run(query.prompt)}