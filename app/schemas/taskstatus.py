from enum import Enum

class TaskStatus(str,Enum):
    PENDING="pending"
    RUNNING="running"
    COMPLETED="completed"
    FAILED="failed"


ALLOWED_TRANSITIONS:dict[TaskStatus,set[TaskStatus]]={
    TaskStatus.PENDING:{TaskStatus.RUNNING},
    TaskStatus.RUNNING:{TaskStatus.COMPLETED,TaskStatus.FAILED},
    TaskStatus.COMPLETED:set(),
    TaskStatus.FAILED:set()
}


    
