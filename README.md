Task Tracker CLI

A Command-Line Interface (CLI) application to track and manage tasks. You can add, update, delete, and mark tasks as in-progress or done, and filter tasks based on their status. This project helps practice CLI programming, file handling, and JSON data storage.

Features

Add new tasks

Update existing tasks

Delete tasks

Mark tasks as in-progress or done

List all tasks

List tasks filtered by status: todo, in-progress, or done

Tasks are stored in a JSON file (tasks.json) in the project directory

Task Properties

Each task has the following properties:

Property	Description
id	Unique identifier for the task
description	Short description of the task
status	Current status: todo, in-progress, done
createdAt	Date and time the task was created
updatedAt	Date and time the task was last updated
Installation

Clone this repository:

git clone <repository-url>
cd task-tracker-cli


Ensure you have Python 3 installed:

python --version

Usage

Run commands from the terminal using Python:

Add a task
python task_cli.py add "Buy groceries"

Update a task
python task_cli.py update 1 "Buy groceries and cook dinner"

Delete a task
python task_cli.py delete 1

Mark task as in-progress
python task_cli.py mark-in-progress 1

Mark task as done
python task_cli.py mark-done 1

List all tasks
python task_cli.py list

List tasks by status
python task_cli.py list todo
python task_cli.py list in-progress
python task_cli.py list done

JSON Storage

Tasks are stored in tasks.json in the current directory.

The file is automatically created if it does not exist.

All task updates reflect immediately in the JSON file.

Error Handling

Handles invalid task IDs gracefully.

Avoids crashing when the JSON file is empty or missing.

Prevents duplicate task IDs by generating unique IDs automatically.

Future Improvements

Add priority levels for tasks

Support due dates and reminders

Export tasks to CSV or PDF

Add interactive CLI menu
