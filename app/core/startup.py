from app.main import app
from app.core.logger import logger
from app.core.config import setting
from app.infra.db.startup_scan import scan

@app.on_event("startup")
async def startup():
    logger.info(f"App just started:{setting.APP_NAME}")
    scan()

    