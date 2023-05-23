from typing import List
from Schema.task_schema import TaskSchema
from Config.db import engine
from fastapi import APIRouter, status, Response
from Model.task_model import tasks

task = APIRouter()


@task.post("/api/task", status_code=status.HTTP_201_CREATED)
async def create_task(data_task: TaskSchema):
    with engine.connect() as conn:
        nuevo = data_task.dict()
        conn.execute(tasks.insert().values(nuevo))
        conn.commit()
    return  Response(status_code=status.HTTP_201_CREATED)

@task.put("/api/task/{task_id}", status_code=status.HTTP_200_OK)
async def update_task(task_id: int, data_task: TaskSchema):
    with engine.connect() as conn:
        # Obtener la tarea existente de la base de datos
        existing_task = conn.execute(tasks.select().where(tasks.c.id == task_id)).fetchone()

        # Verificar si la tarea existe
        if existing_task:
            # Actualizar los campos de la tarea con los datos nuevos
            update_data = data_task.dict(exclude_unset=True)
            conn.execute(tasks.update().where(tasks.c.id == task_id).values(**update_data))
            conn.commit()
            return Response(status_code=status.HTTP_200_OK)
        else:
            return Response(status_code=status.HTTP_404_NOT_FOUND)
        
@task.delete("/api/task/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int):
    with engine.connect() as conn:
        # Verificar si la tarea existe
        existing_task = conn.execute(tasks.select().where(tasks.c.id == task_id)).fetchone()

        if existing_task:
            # Eliminar la tarea de la base de datos
            conn.execute(tasks.delete().where(tasks.c.id == task_id))
            conn.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status_code=status.HTTP_404_NOT_FOUND)
        
@task.get("/api/tasks", response_model=List[TaskSchema])
async def list_tasks():
    with engine.connect() as conn:
        # Obtener todas las tareas de la base de datos
        query = tasks.select()
        result = conn.execute(query).fetchall()

        # Convertir los resultados en una lista de diccionarios
        tasks_list = [dict(row._asdict()) for row in result]

        return tasks_list
