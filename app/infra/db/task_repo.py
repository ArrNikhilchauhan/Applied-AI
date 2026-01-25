from sqlalchemy import text
from datetime import datetime,timezone
import uuid
from app.infra.db.database import get_db

class TaskRepo:
    def __init__(self,db):
        self.db=db
        

    def create(self,task_id,prompt):
        query=text("insert into tasks(task_id,status,prompt)values(:task_id,:status,:prompt)")
        self.db.execute(query,{"task_id":task_id,"status":"Pending","prompt":prompt})
        self.db.commit()

    def set_running(self,task_id,prompt):
        query=text("update tasks set status=:status,prompt=:prompt,updated_at=:now where task_id=:task_id")
        self.db.execute(query,{"status":"running","prompt":prompt,"now":datetime.now(timezone.utc),"task_id":task_id})
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
        query=text("select * from tasks where task_id=:task_id")
        result=self.db.execute(query,{"task_id":task_id})
        row = result.mappings().first()
        return row
