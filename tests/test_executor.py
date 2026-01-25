from app.infra.db.database import sessionlocal
import uuid
from sqlalchemy import text
from app.infra.db.task_repo import TaskRepo
from app.api.dependencies import get_llm
from app.services.agent_service import AgentService
from app.services.agent_executor import run_agent_task
from app.core.config import setting
import pytest


@pytest.mark.asyncio
async def test_executor_owns_session():

    task_id = str(uuid.uuid4())
    prompt = "hello"


    db = sessionlocal()
    try:
        db.execute(
            text("""
            select * from tasks
            """)
        )
        db.commit()
    finally:
        db.close() 


    agent_service=AgentService(get_llm(setting.LLM_PROVIDER))
    await run_agent_task(agent_service,task_id, prompt)


    db = sessionlocal()
    try:
        row = db.execute(
            text("SELECT status FROM tasks WHERE task_id = :task_id"),
            {"task_id": task_id}
        ).scalar_one()
    finally:
        db.close()

    assert row=="completed"
