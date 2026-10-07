import json
from pathlib import Path

from .task import Task

TASK_FILE = Path("tasks.json")


def read_file():
    try:
        with TASK_FILE.open("r") as file:
            data = json.load(file)
            return {
                int(task_id): Task.model_validate(task_data)
                for task_id, task_data in data.items()
            }

    except FileNotFoundError:
        TASK_FILE.write_text("{}")
        return {}

    except json.JSONDecodeError as error:
        raise ValueError("tasks.json contains invalid JSON") from error


def update_file(tasks: dict[int, Task]):
    try:
        with TASK_FILE.open("w") as file:
            json.dump(
                {
                    task_id: task.model_dump(mode="json")
                    for task_id, task in tasks.items()
                },
                file,
                indent=4,
            )
    except FileNotFoundError:
        TASK_FILE.write_text("{}")
        return {}

    except json.JSONDecodeError as error:
        raise ValueError("tasks.json contains invalid JSON") from error
