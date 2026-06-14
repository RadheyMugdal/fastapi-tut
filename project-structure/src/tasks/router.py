from fastapi import APIRouter,Depends
from src.tasks import controller
from src.tasks.dtos import TaskCreate
from src.utils.db import get_db

task_routes=APIRouter(prefix="/tasks",tags=["tasks"])

@task_routes.post("/")
def create_task(data:TaskCreate,db=Depends(get_db)):
    return controller.create_task(data,db) 

@task_routes.get("/")
def get_tasks(db=Depends(get_db)):
    return controller.get_tasks(db)

@task_routes.get("/{id}")
def get_task(id:int,db=Depends(get_db)):
    return controller.get_task(id,db)