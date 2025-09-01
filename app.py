from fastapi import FastAPI, HTTPException, Query
from typing import List 
from models import CreateTask, UpdateTask, TaskStatus, Task, Importance

app = FastAPI(title="CRUD_tasks")

tasks = {}
id_count = 1


@app.post("/create_task", response_model=Task)
def create_task(
    request_task: CreateTask):
    global id_count
    new_task = Task(id=id_count, **request_task.dict())
    tasks[id_count] = new_task
    id_count += 1
    return new_task


@app.get("/list_tasks", response_model=List[Task])
def tasks_list(
    status: TaskStatus | None = Query(None, description = "Фильтр по статусу"),
    importance:  Importance | None = Query(None, description = "Фильтр по важности")
):
    query_list = list(tasks.values())
    if status:
        query_list = [t for t in query_list if t.status == status]
    if importance:
        query_list = [t for t in query_list if t.importance == importance]
    return query_list 


@app.get("/get_task/{id}", response_model=Task)
def get_task(id: int):
    if id not in tasks:
        raise HTTPException(404, "Not found")
    return tasks[id]


@app.put("/update_task/{id}", response_model=Task) 
def update_task(id: int, updated_task: UpdateTask):
    if id not in tasks:
        raise HTTPException(404, "Not found")
    task = tasks[id]  
    
    if updated_task.name is not None: 
        task.name = updated_task.name
    if updated_task.time is not None: 
        task.time = updated_task.time
    if updated_task.importance is not None:
        task.importance = updated_task.importance
    if updated_task.status is not None:
        task.status = updated_task.status
    
    return task


@app.delete("/delete_task/{id}", status_code=204) 
def delete_task(id: int):
    if id not in tasks:
        raise HTTPException(404, "Not found")
    tasks.pop(id)

    return None
