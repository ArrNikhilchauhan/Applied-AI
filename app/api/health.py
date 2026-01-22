from fastapi import APIRouter,Depends
from app.core.logger import logger
from app.services.system_service import SystemService
from app.schemas.system_schema import HealthResponse,HealthScoreResponse

router=APIRouter()

def get_system_service():
    return SystemService()

@router.get('/health',response_model=HealthResponse)
def health(system_ser=Depends(get_system_service)):
    logger.info("Process Started")
    return system_ser.health()



@router.get('/health_score',response_model=HealthScoreResponse)
def healthscore(system_ser=Depends(get_system_service)):
    logger.info("Health score called")
    return system_ser.health_score()
