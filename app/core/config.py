from pydantic_settings import BaseSettings,SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    APP_NAME:str=Field(...,description="App Name")
    SECRET:str
    LOGGING_LEVEL:str
    DEBUG:bool=False
    LLM_PROVIDER:str="dummy"
    DB_USER:str
    DB_PASSWORD:str
    DB_HOST:str
    DB_PORT:int
    DB_NAME:str

    model_config=SettingsConfigDict(
        env_file='.env'
    )

setting=Settings()