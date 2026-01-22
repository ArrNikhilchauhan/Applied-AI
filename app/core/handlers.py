from fastapi import Request,Depends
from fastapi.responses import JSONResponse
from app.core.logger import logger
from app.core.exceptions import AppException
from app.schemas.error import ErrorResponse

async def app_exception_handler(req:Request,exc:AppException):
    logger.error(f"{exc.message}")
    error_message=ErrorResponse(error=exc.message)
    return JSONResponse(
        status_code=exc.status_code,
        content=error_message.model_dump()
    )