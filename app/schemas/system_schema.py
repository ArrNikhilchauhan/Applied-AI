from pydantic import BaseModel,Field

class HealthResponse(BaseModel):
    app:str=Field(description="App Name")
    status:str
    service:str

class HealthScoreResponse(BaseModel):
    health:int
    accuracy:float
    app:str