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

    new_status="completed"
    agent_service=AgentService(get_llm(setting.LLM_PROVIDER))
    repo=TaskRepo(db)
    repo.create(task_id,prompt)
    repo.set_running(task_id)
    repo.update_status(task_id,new_status)


    db = sessionlocal()
    try:
        row = db.execute(
            text("SELECT status FROM tasks WHERE task_id = :task_id"),
            {"task_id": task_id}
        ).scalar_one()
    finally:
        db.close()

    assert row=="completed"
