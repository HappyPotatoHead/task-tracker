from datetime import datetime, timezone

from .process_file import read_file, update_file
from .task import Task, TaskStatus

task_database: dict[int, Task] = {}
task_statuses: dict[TaskStatus, set[int]] = {
    TaskStatus.TODO: set(),
    TaskStatus.IN_PROGRESS: set(),
    TaskStatus.DONE: set(),
}


def load_tasks():
    task_database.update(read_file())
    if task_database:
        Task._next_id = max(task_database) + 1

    for task in task_database.values():
        task_statuses[task.status].add(task.id)


def create_task(description: str) -> Task:
    task = Task(description=description)
    task_database[task.id] = task
    task_statuses[TaskStatus.TODO].add(task.id)
    update_file(task_database)
    return task


# let's imagine that there is a
def update_task(id: int, description: str) -> Task:
    updated_task = task_database.get(id)

    if updated_task is None:
        raise ValueError(f"Task {id} does not exist")

    updated_task.description = description
    updated_task.updatedAt = datetime.now(timezone.utc)
    update_file(task_database)

    return updated_task


def delete_task(id: int):
    if id not in task_database:
        raise ValueError(f"Task {id} does not exist")

    del task_database[id]
    update_file(task_database)


def update_status(id: int, status: TaskStatus):
    task = task_database.get(id)

    if task is None:
        raise ValueError(f"Task {id} does not exist")

    task_statuses[task.status].remove(id)

    task.status = status
    task.updatedAt = datetime.now(timezone.utc)
    task_statuses[status].add(id)

    update_file(task_database)


def list_task(status: TaskStatus | None = None) -> None:
    if status is None:
        for value in task_database.values():
            print(value)

        return

    for id in task_statuses[status]:
        print(task_database[id])
