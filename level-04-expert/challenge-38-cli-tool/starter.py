import argparse
import json
import os
import sys

DEFAULT_FILE = "tasks.json"


def load_tasks(filepath=DEFAULT_FILE):
    if not os.path.exists(filepath):
        return []

    with open(filepath, "r") as f:
        return json.load(f)


def save_tasks(tasks, filepath=DEFAULT_FILE):
    with open(filepath, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(title, priority="medium", filepath=DEFAULT_FILE):
    tasks = load_tasks(filepath)

    next_id = max(t["id"] for t in tasks) + 1 if tasks else 1

    task = {
        "id": next_id,
        "title": title,
        "priority": priority,
        "done": False
    }

    tasks.append(task)
    save_tasks(tasks, filepath)

    return task


def list_tasks(priority=None, filepath=DEFAULT_FILE):
    tasks = load_tasks(filepath)

    if priority is not None:
        tasks = [t for t in tasks if t["priority"] == priority]

    return tasks


def complete_task(task_id, filepath=DEFAULT_FILE):
    tasks = load_tasks(filepath)

    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks, filepath)
            return True

    return False


def delete_task(task_id, filepath=DEFAULT_FILE):
    tasks = load_tasks(filepath)

    original_len = len(tasks)

    tasks = [t for t in tasks if t["id"] != task_id]

    if len(tasks) == original_len:
        return False

    save_tasks(tasks, filepath)
    return True


def build_parser():
    parser = argparse.ArgumentParser(
        prog="tasks",
        description="Simple task manager CLI"
    )

    subparsers = parser.add_subparsers(dest="command")


    add_parser = subparsers.add_parser(
        "add",
        help="Add a new task"
    )

    add_parser.add_argument(
        "title",
        help="Task title"
    )

    add_parser.add_argument(
        "--priority",
        choices=["high", "medium", "low"],
        default="medium"
    )


    list_parser = subparsers.add_parser(
        "list",
        help="List tasks"
    )

    list_parser.add_argument(
        "--priority",
        choices=["high", "medium", "low"]
    )


    complete_parser = subparsers.add_parser(
        "complete",
        help="Mark task as complete"
    )

    complete_parser.add_argument(
        "id",
        type=int
    )


    delete_parser = subparsers.add_parser(
        "delete",
        help="Delete a task"
    )

    delete_parser.add_argument(
        "id",
        type=int
    )


    return parser


def main():

    parser = build_parser()
    args = parser.parse_args()


    if args.command is None:
        parser.print_help()
        sys.exit(1)


    if args.command == "add":

        task = add_task(
            args.title,
            args.priority
        )

        print(
            f"Added task #{task['id']}: '{task['title']}' [{task['priority']}]"
        )


    elif args.command == "list":

        tasks = list_tasks(args.priority)

        for t in tasks:
            print(
                f"#{t['id']} [{'x' if t['done'] else ' '}] "
                f"{t['title']} [{t['priority']}]"
            )


    elif args.command == "complete":

        if complete_task(args.id):
            print(f"Task #{args.id} marked as complete.")
        else:
            print(f"Task #{args.id} not found.")


    elif args.command == "delete":

        if delete_task(args.id):
            print(f"Task #{args.id} deleted.")
        else:
            print(f"Task #{args.id} not found.")



if __name__ == "__main__":
    main()