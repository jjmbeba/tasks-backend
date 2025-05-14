from fastapi import FastAPI, HTTPException, status
from models import Task, TaskCreate
from typing import List

app = FastAPI()

tasks : List[Task] = []
next_task_id = 1

@app.get('/')
def read_root():
    return {
        "Hello": "World"
    }

@app.get('/tasks')
def get_all_tasks():
    return tasks

@app.post('/tasks', response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task_input: TaskCreate):
    global next_task_id

    new_task = Task(
        id=next_task_id,
        name=task_input.name,
        description=task_input.description
    )

    tasks.append(new_task)
    next_task_id += 1

    return new_task

@app.delete('/tasks/{task_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    task_index = next((index for index, task in enumerate(tasks) if task.id == task_id ), -1)

    if task_index == -1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID {task_id} does not exist."
        )
    
    del tasks[task_index]

    return None