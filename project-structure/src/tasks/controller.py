from src.tasks.dtos import TaskCreate
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel
from src.tasks.dtos import TaskCreate,TaskUpdate
from fastapi import HTTPException

def create_task(body:TaskCreate,db:Session):
    data=body.model_dump()
    new_task=TaskModel(title=data["title"],description=data["description"],is_completed=data["is_completed"])
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


def get_tasks(db:Session):
    tasks=db.query(TaskModel).all()
    return tasks


def get_task(id:int,db:Session):
    task=db.query(TaskModel).get(id)
    if not task:
        return HTTPException(status_code=404,detail="task with id: {} not found".format(id))
    return task



def update_task(body:TaskUpdate,task_id:int,db:Session):
    task=db.query(TaskModel).get(task_id)
    if not task:
        return HTTPException(status_code=404,detail="task with id: {} not found".format(id))

    update_data=body.model_dump(exclude_unset=True)
    for key,value in update_data.items():
        setattr(task,key,value)

    db.commit()
    db.refresh(task)

    return task


def delete_task(id:int,db:Session):
    task=db.query(TaskModel).get(id)
    if not task:
        return HTTPException(404,detail=f"task with id: {id} not found")
    db.delete(task)
    db.commit()
    return None