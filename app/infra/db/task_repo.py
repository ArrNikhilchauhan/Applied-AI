from sqlalchemy import text
from datetime import datetime,timezone
import uuid
from app.core.exceptions import AppException
from app.schemas.taskstatus import TaskStatus,ALLOWED_TRANSITIONS

class TaskRepo:
    def __init__(self,db):
        self.db=db

    def create(self,task_id,prompt):
        query=text("insert into tasks(task_id,status,prompt)values(:task_id,:status,:prompt)")
        self.db.execute(query,{"task_id":task_id,"status":"pending","prompt":prompt})
        self.db.commit()

    def set_running(self,task_id):
        query=text("update tasks set status=:status,updated_at=:now where task_id=:task_id")
        self.db.execute(query,{"status":"running","now":datetime.now(timezone.utc),"task_id":task_id})
        self.db.commit()
        
    def set_completed(self,task_id,result):
        query=text("update tasks set status=:status,result=:result,updated_at=:now where task_id=:task_id")
        self.db.execute(query,{"status":"completed","result":result,"now":datetime.now(timezone.utc),"task_id":task_id})
        self.db.commit()

    def set_failed(self,task_id,error):
        query=text("update tasks set status=:status,error=:error,updated_at=:now where task_id=:task_id")
        self.db.execute(query,{"status":"Failed","error":error,"now":datetime.now(timezone.utc),"task_id":task_id})
        self.db.commit()

    def get(self,task_id:uuid):
        query=text("select status from tasks where task_id=:task_id")
        result=self.db.execute(query,{"task_id":task_id})
        row = result.mappings().first()
        return row
    
    def update_status(self,task_id:uuid,new_status):
        row=self.get(task_id)
        status=TaskStatus(row.status)

        allowed=ALLOWED_TRANSITIONS[status]

        methods_allowed=[s for s in allowed]
        
        if row.status in ["completed","failed"]:
            return row

        if new_status not in methods_allowed:
            raise AppException("Unauthorized",401)
        
        query = text("""
        UPDATE tasks
        SET status = :status, updated_at = :now
        WHERE task_id = :task_id
    """)

        self.db.execute(query, {
        "status": new_status,
        "now": datetime.now(timezone.utc),
        "task_id": task_id
    })
        self.db.commit()

    def create_if_not_exist(self,task_id:uuid,prompt:str):
        row=self.get(task_id)
        if row:
            return row
        
        query=text("insert into tasks (task_id,status,prompt) values (:task_id,:status,:prompt)")

        self.db.execute(query,{"task_id":task_id,"status":"pending","prompt":prompt})
        self.db.commit()

    def retry(self,task_id:uuid):
        row=self.get(task_id)
        if row.status!="failed":
            return row
        else:
            self.update_status(task_id,"running")
            
        
            

        
        

        

        

        
        


