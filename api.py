from fastapi import FastAPI
from schemas import TaskRequest, TaskResponse
from service import OpenPlanterService

app = FastAPI(title="OpenPlanter API")

service = OpenPlanterService()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/task", response_model=TaskResponse)
def run_task(request: TaskRequest):
    result = service.solve(request.task)
    return TaskResponse(result=result)