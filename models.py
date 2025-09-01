from pydantic import BaseModel, Field
from enum import Enum
from typing import Union, List

#___ПЕРЕЧИСЛЕНИЯ___

class Importance(str, Enum):
    low = "низкий приоритет"
    medium = "средний приоритет"
    high = "высокий приоритет"
    extremly = "чрезвычайный приоритет"
    
class TaskStatus(str, Enum):
    raw = "не выполняется❌"
    running = "выполняется🔄"
    solved = "выполнено✅"

#___Тела___

class CreateTask(BaseModel):
    name: str = Field(
        ...,
        min_length = 1,
        max_length = 100,
        description = "Название задачи (до 100 символов)"
    )
    
    time: int = Field(
        ...,
        ge = 1,
        le = 100,
        description = "Время на выполнение в днях"
    )
    
    importance: Importance = Field(
        Importance.medium,
        description = "Важность задачи в enum (low, medium, high, extremely)"
    )
    
    status: TaskStatus = Field(
        TaskStatus.raw,
        description = "Статус задачи в enum (не выполняется❌, выполняется🔄, выполнено✅)"
    )

class UpdateTask(BaseModel):
    name: str | None = Field(
        None,
        min_length = 1,
        max_length = 100,
        description = "Название задачи (до 100 символов)"
    )
    
    time: int | None = Field(
        None,
        ge = 1,
        le = 100,
        description = "Время на выполнение в днях"
    )
    
    importance: Importance | None = Field(
        None,
        description = "Важность задачи в enum (low, medium, high, extremely)"
    )
    
    status: TaskStatus | None = Field(
        None,
        description = "Статус задачи в enum (не выполняется❌, выполняется🔄, выполнено✅)"
    )

class Task(CreateTask):
    id: int
    