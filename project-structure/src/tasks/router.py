from fastapi import APIRouter,Depends,status
from src.tasks import controller
from src.tasks.dtos import TaskCreate,TaskUpdate,TaskResponse
from src.utils.db import get_db
from src.tasks.models import TaskModel
from typing import List
from sqlalchemy.orm import Session

task_routes=APIRouter(prefix="/tasks",tags=["tasks"])

@task_routes.post("/",status_code=status.HTTP_201_CREATED,response_model=TaskResponse)
def create_task(data:TaskCreate,db:Session=Depends(get_db)):
    return controller.create_task(data,db) 

@task_routes.get("/",status_code=status.HTTP_200_OK,response_model=List[TaskResponse])
def get_tasks(db=Depends(get_db)):
    return controller.get_tasks(db)

@task_routes.get("/{id}",status_code=status.HTTP_200_OK,response_model=TaskResponse)
def get_task(id:int,db:Session=Depends(get_db)):
    return controller.get_task(id,db)

@task_routes.patch("/{id}",status_code=status.HTTP_201_CREATED,response_model=TaskResponse)
def update_task(id:int,body:TaskUpdate,db:Session=Depends(get_db)):
    return controller.update_task(body=body,db=db,task_id=id)   

@task_routes.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id:int,db:Session=Depends(get_db)):
    return controller.delete_task(id,db)