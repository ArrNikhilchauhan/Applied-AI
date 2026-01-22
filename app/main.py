from fastapi import FastAPI
from app.core.logger import logger
#from dotenv import load_dotenv # this shouldn't be imported here because main only wire app it can lead to multiple unncessary import which  make the system slow
from app.api.health import health_router  # always import from root package not from relative this is wrong
# from app.api.health import router this is correct
from app.core.config import setting
from app.api.llm import llm_router
from app.core.handlers import app_exception_handler
from app.core.exceptions import AppException

app=FastAPI()

@app.on_event("startup")
async def startup():
    logger.info(f"App Startup APP_NAME:{setting.APP_NAME}")

@app.on_event("shutdown")
async def shutdown():
    logger.info("App Shutdown")


app.include_router(router=health_router,prefix='/api',tags=["system"])
app.include_router(router=llm_router,prefix='/api/llm')
app.add_exception_handler(AppException,app_exception_handler)


