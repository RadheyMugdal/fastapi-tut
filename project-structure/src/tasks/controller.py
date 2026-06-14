from src.tasks.dtos import TaskCreate
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel
from fastapi import HTTPException

def create_task(body:TaskCreate,db:Session):
    data=body.model_dump()
    new_task=TaskModel(title=data["title"],description=data["description"],is_completed=data["is_completed"])
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {"status":"Task created successfully","data":new_task}


def get_tasks(db:Session):
    tasks=db.query(TaskModel).all()
    return {"status":"Tasks retrieved successfully","data":tasks} 


def get_task(id:int,db:Session):
    task=db.query(TaskModel).get(id)
    if not task:
        return HTTPException(status_code=404,detail="task with id: {} not found".format(id))
    return {"status":f"Successfully fetched task with id {id}","task":task}