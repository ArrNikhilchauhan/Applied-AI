from pydantic_settings import BaseSettings,SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    APP_NAME:str=Field(...,description="App Name")
    SECRET:str
    LOGGING_LEVEL:str
    DEBUG:bool=False

    model_config=SettingsConfigDict(
        env_file='.env'
    )

setting=Settings()