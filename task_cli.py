import json
import os
import argparse
from datetime import datetime

# JSON file to store tasks
TASK_FILE = "tasks.json"

# Ensure JSON file exists
if not os.path.exists(TASK_FILE):
    with open(TASK_FILE, "w") as f:
        json.dump([], f)

# Load tasks from JSON file
def load_tasks():
    with open(TASK_FILE, "r") as f:
        return json.load(f)

# Save tasks to JSON file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Generate a new unique ID
def generate_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1

# Add a new task
def add_task(description):
    tasks = load_tasks()
    task_id = generate_id(tasks)
    now = datetime.now().isoformat()
    task = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task_id})")

# Update a task
def update_task(task_id, description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully")
            return
    print(f"Task with ID {task_id} not found!")

# Delete a task
def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]
    if len(new_tasks) == len(tasks):
        print(f"Task with ID {task_id} not found!")
        return
    save_tasks(new_tasks)
    print(f"Task {task_id} deleted successfully")

# Mark task as in progress
def mark_in_progress(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "in-progress"
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} marked as in-progress")
            return
    print(f"Task with ID {task_id} not found!")

# Mark task as done
def mark_done(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} marked as done")
            return
    print(f"Task with ID {task_id} not found!")

# List tasks
def list_tasks(filter_status=None):
    tasks = load_tasks()
    filtered = tasks
    if filter_status:
        filtered = [task for task in tasks if task["status"] == filter_status]
    if not filtered:
        print("No tasks found!")
        return
    for task in filtered:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, CreatedAt: {task['createdAt']}, UpdatedAt: {task['updatedAt']}")

# CLI Argument parsing
def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Add task
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("description", type=str, help="Description of the task")

    # Update task
    update_parser = subparsers.add_parser("update")
    update_parser.add_argument("id", type=int, help="ID of the task")
    update_parser.add_argument("description", type=str, help="New description of the task")

    # Delete task
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("id", type=int, help="ID of the task")

    # Mark in-progress
    in_progress_parser = subparsers.add_parser("mark-in-progress")
    in_progress_parser.add_argument("id", type=int, help="ID of the task")

    # Mark done
    done_parser = subparsers.add_parser("mark-done")
    done_parser.add_argument("id", type=int, help="ID of the task")

    # List tasks
    list_parser = subparsers.add_parser("list")
    list_parser.add_argument("status", nargs="?", choices=["todo", "in-progress", "done"], help="Filter by status")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description)
    elif args.command == "update":
        update_task(args.id, args.description)
    elif args.command == "delete":
        delete_task(args.id)
    elif args.command == "mark-in-progress":
        mark_in_progress(args.id)
    elif args.command == "mark-done":
        mark_done(args.id)
    elif args.command == "list":
        list_tasks(args.status)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
