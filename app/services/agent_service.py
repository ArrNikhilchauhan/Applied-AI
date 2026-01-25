import asyncio
from app.infra.llm.base import BaseLLM

class AgentService:
    def __init__(self,llm:BaseLLM):
        self.llm=llm

    
    def run_sync(self,prompt:str):
        return self.llm.generate(prompt)
    
    async def run_async(self):
        return await asyncio.to_thread(self.run_sync)
    