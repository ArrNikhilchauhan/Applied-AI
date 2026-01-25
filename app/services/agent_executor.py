from app.services.agent_service import AgentService
from app.infra.db.task_repo import TaskRepo
from app.infra.db.database import sessionlocal

def run_agent_task(
        service:AgentService,
        task_id:str,
        prompt:str
):
    db=sessionlocal()
    store=TaskRepo(db)
    store.create(task_id,prompt)
    store.set_running(task_id,prompt)
    try:
        res=service.run_sync(prompt)
        store.set_completed(task_id,res)
    except Exception as e:
        store.set_failed(task_id,e)
    finally:
        db.close()
    

def check_status(
        task_id:str,
        store=TaskRepo
):
    result=store.get(task_id)
    return result
