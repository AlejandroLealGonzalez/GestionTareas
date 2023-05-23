from fastapi import FastAPI
from Router.task_router import task

app = FastAPI()

app.include_router(task)