from app.services.agent_service import AgentService
from app.infra.db.task_repo import TaskRepo
from app.infra.db.database import sessionlocal

def run_agent_task(
        service:AgentService,
        task_id:str,
        prompt:str,
        new_status:str
):
    db=sessionlocal()
    store=TaskRepo(db)
    store.create_if_not_exist(task_id,prompt)
    try:
        res=service.run_sync(prompt)
        store.update_status(task_id,new_status)
    except Exception as e:
        retry=3
        error=None
        for _ in range(3):
            success=False
            try:
                res=service.run_sync(prompt)
                store.set_completed(task_id,res)
                return 
            except Exception as e:
                error=e

        if not success:
            store.set_failed(task_id,error)
    finally:
        db.close()
    

def check_status(
        task_id:str
):
    db=sessionlocal()
    store=TaskRepo(db)
    result=store.get(task_id)
    return result
