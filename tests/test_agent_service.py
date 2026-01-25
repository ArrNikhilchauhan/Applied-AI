import uuid
import pytest
from app.services.agent_service import AgentService
from tests.test_llm_service import fake_llm
from app.core.task_store import task_store
from app.services.agent_executor import run_agent_task

# @pytest.mark.asyncio
# async def test_background_execution():
#     store = task_store
#     llm = fake_llm()
#     service = AgentService(llm)
#     task_id=str(uuid.uuid4())

#     await run_agent_task(service,task_id,"Heloo",store)

    

#     assert store.status(task_id)["status"] == "completed"
