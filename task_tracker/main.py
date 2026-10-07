import argparse

from .task import TaskStatus
from .task_service import (
    create_task,
    delete_task,
    list_task,
    load_tasks,
    update_status,
    update_task,
)


def main():
    load_tasks()

    parser = argparse.ArgumentParser(prog="task-cli")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # create_parser
    create_parser = subparsers.add_parser("add")
    create_parser.add_argument("description")

    # list_parser
    list_parser = subparsers.add_parser("list")
    list_parser.add_argument("status", nargs="?", type=TaskStatus)

    # update_parser
    update_parser = subparsers.add_parser("update")
    update_parser.add_argument("id", type=int)
    update_parser.add_argument("description")

    # delete_parser
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("id", type=int)

    # status_parser
    in_progress_parser = subparsers.add_parser("mark-in-progress")
    in_progress_parser.add_argument("id", type=int)

    done_parser = subparsers.add_parser("mark-done")
    done_parser.add_argument("id", type=int)

    todo_parser = subparsers.add_parser("todo")
    todo_parser.add_argument("id", type=int)

    args = parser.parse_args()

    if args.command == "add":
        task = create_task(args.description)
        print(f"Task added successfully (ID: {task.id})")
    elif args.command == "update":
        update_task(args.id, args.description)
    elif args.command == "delete":
        delete_task(args.id)
    elif args.command == "mark-in-progress":
        update_status(args.id, TaskStatus.IN_PROGRESS)
    elif args.command == "mark-done":
        update_status(args.id, TaskStatus.DONE)
    elif args.command == "todo":
        update_status(args.id, TaskStatus.TODO)
    elif args.command == "list":
        list_task(args.status)


# add cli later on
if __name__ == "__main__":
    main()
