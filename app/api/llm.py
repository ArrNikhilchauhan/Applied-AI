from fastapi import APIRouter
from app.schemas.ai import PromptRequest

llm_router=APIRouter()

@llm_router.post('/prompt')
def prompt(query:PromptRequest):
    return{
        "recieved":query.prompt
    }