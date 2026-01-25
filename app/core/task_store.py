from typing import Any, Dict
from app.infra.db.task_repo import TaskRepo

class TaskStore:
    def __init__(self):
        self._tasks: Dict[str, Dict[str, Any]] = {}

    def create(self, task_id: str):
        self._tasks[task_id] = {
            "status": "pending",
            "result": None,
            "error": None,
        }

    def set_running(self, task_id: str):
        self._tasks[task_id]["status"] = "running"

    def set_completed(self, task_id: str,result:Any):
        self._tasks[task_id]["status"] = "completed"
        self._tasks[task_id]["result"] = result

    def set_failed(self, task_id: str,error:Any):
        self._tasks[task_id]["status"] = "failed"
        self._tasks[task_id]["error"] = error

    def status(self, task_id: str) -> Dict[str, Any] | None:
        return self._tasks.get(task_id)


task_store = TaskStore()

# def check_status(task_id):
#     response=task_store.status(task_id)
#     if not response:
#         raise AppException("Invalid Task ID",500)
#     if response["status"]=="completed":
#         return response["result"]
#     elif response["status"]=="failed":
#         return response["error"]
        
#     return response
