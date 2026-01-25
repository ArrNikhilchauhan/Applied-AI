from app.infra.db.database import sessionlocal
from sqlalchemy import text



def scan():
    db=sessionlocal()
    try:
        query=text("update tasks set status=:new_status where status=:old_status")
        db.execute(query,{"new_status":"Failed","old_status":"running"})
        db.commit()
    finally:
        db.close()
