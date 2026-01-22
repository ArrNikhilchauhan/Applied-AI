from app.core.config import setting
from app.schemas.system_schema import HealthResponse,HealthScoreResponse

class SystemService:
    def __init__(self):
        pass

    def health_score(self):
        return HealthScoreResponse( health=90,
            accuracy=54,
            app=setting.APP_NAME
            )
    
    def health(self):
        return HealthResponse(
        app=setting.APP_NAME,
        staus= "ok",
        service= "applied-ai-system"
        )
        
        
