from app.core.exceptions import AppException
from app.infra.db.task_repo import TaskRepo
import uuid
from app.infra.db.database import sessionlocal
import pytest


def test_enforcemnt():
    task_id=uuid.uuid4()
    db=sessionlocal()

    repo=TaskRepo(db)

    repo.create(task_id,"hello")

    with pytest.raises(AppException):
        res=repo.update_status(task_id,"Completed")

    