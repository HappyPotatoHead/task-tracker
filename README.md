# Task Tracker

A command-line task tracker built with Python.

Tasks are persisted to a local JSON file and support creating, updating, deleting, and filtering tasks by status.

## Features

- Add tasks
- Update task descriptions
- Delete tasks
- Mark tasks as in progress or done
- List all tasks
- Filter tasks by status
- Persist tasks to JSON
- Automatic task IDs
- Task creation and update timestamps
- Input validation with Pydantic

## Requirements

- Python 3.10+
- Pydantic 2.x

## Installation

Clone the repository and install it in editable mode:

```bash
git clone <repository-url>
cd task-tracker
pip install -e .
```

This installs the `task-cli` command.

## Usage

### Add a task

```bash
task-cli add "Buy groceries"
```

```text
Task added successfully (ID: 1)
```

### List tasks

```bash
task-cli list
```

### Update a task

```bash
task-cli update 1 "Buy groceries and cook dinner"
```

### Mark a task as in progress

```bash
task-cli mark-in-progress 1
```

### Mark a task as done

```bash
task-cli mark-done 1
```

### Filter by status

```bash
task-cli list todo
task-cli list in-progress
task-cli list done
```

### Delete a task

```bash
task-cli delete 1
```

## Project Structure

```text
task-tracker/
├── pyproject.toml
├── task_tracker/
│   ├── __init__.py
│   ├── main.py
│   ├── task.py
│   ├── task_service.py
│   └── process_file.py
├── tasks.json
└── README.md
```

### Architecture

The project is separated into three main layers:

- **CLI (`main.py`)**: Parses command-line arguments and handles user-facing output.
- **Service (`task_service.py`)**: Contains task management and business logic.
- **Persistence (`process_file.py`)**: Handles reading and writing tasks to JSON.

Tasks are kept in memory using a dictionary and persisted to `tasks.json`.

## Tech Stack

- Python
- Pydantic
- argparse
- JSON
- setuptools

# Credit

https://roadmap.sh/projects/task-tracker
