from app.core.config import setting
from app.schemas.system_schema import HealthResponse,HealthScoreResponse
from app.core.exceptions import AppException

class SystemService:
    def __init__(self):
        pass

    def health_score(self):
        if True:
            raise AppException("server is down",501)
        return HealthScoreResponse( health=90,
            accuracy=54,
            app=setting.APP_NAME
            )
    
    def health(self):
        return HealthResponse(
        app=setting.APP_NAME,
        status= "ok",
        service= "applied-ai-system"
        )
        
        
