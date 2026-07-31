from pydantic import BaseModel


class TaskRequest(BaseModel):
    task: str


class TaskResponse(BaseModel):
    result: str