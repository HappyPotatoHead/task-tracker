from datetime import datetime, timezone
from enum import Enum
from typing import ClassVar

from pydantic import BaseModel, Field


class TaskStatus(str, Enum):
    TODO = "todo"
    IN_PROGRESS = "in-progress"
    DONE = "done"

    def __str__(self) -> str:
        return self.value


class Task(BaseModel):
    id: int = Field(default_factory=lambda: Task._get_next_id())
    description: str = Field(min_length=1, max_length=500)
    status: TaskStatus = TaskStatus.TODO
    createdAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updatedAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    _next_id: ClassVar[int] = 1

    @classmethod
    def _get_next_id(cls):
        id = cls._next_id
        cls._next_id += 1
        return id

    def __str__(self):
        return f"[{self.id}] {self.description} {self.status}"
