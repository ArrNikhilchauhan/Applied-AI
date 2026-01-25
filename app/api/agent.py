from fastapi import APIRouter,Depends
from app.schemas.ai import PromptRequest
from app.api.dependencies import get_agent_service
from fastapi import BackgroundTasks
from app.services.agent_executor import run_agent_task,check_status
from app.infra.db.task_repo import TaskRepo
import uuid

agent_router=APIRouter()

@agent_router.post('/run')
def run(data:PromptRequest,bg_task:BackgroundTasks,service=Depends(get_agent_service)):
    task_id=str(uuid.uuid4())
    bg_task.add_task(run_agent_task,service,task_id,data.prompt)
    return {"task_id":task_id}



@agent_router.get('/status/{task_id}')
def status(task_id):
    return check_status(task_id,TaskRepo())
    

