from fastapi import FastAPI
from app.core.logger import logger
#from dotenv import load_dotenv # this shouldn't be imported here because main only wire app it can lead to multiple unncessary import which  make the system slow
from app.api.health import router  # always import from root package not from relative this is wrong
# from app.api.health import router this is correct
from app.core.config import setting

app=FastAPI()
logger.info("Main.py just started")
@app.on_event("startup")
async def startup():
    logger.info(f"App Startup APP_NAME:{setting.APP_NAME}")

@app.on_event("shutdown")
async def shutdown():
    logger.info("App Shutdown")
app.include_router(router=router,prefix='/api',tags=["system"])


