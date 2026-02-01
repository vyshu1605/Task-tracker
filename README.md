Project url - [https://github.com/vyshu1605/Task-tracker](https://roadmap.sh/projects/task-tracker)

# Task Tracker CLI 📝

A **Command-Line Interface (CLI)** application to track and manage tasks efficiently.  
Easily **add, update, delete, and mark tasks** as in-progress or done, and filter tasks by status.  
All tasks are stored locally in a **JSON file** for persistence.

---

## Features ✅

- Add new tasks with auto-generated IDs
- Update existing task descriptions
- Delete tasks by ID
- Mark tasks as **in-progress** or **done**
- List all tasks or filter by **status** (`todo`, `in-progress`, `done`)
- Persistent storage in `tasks.json` (auto-created if missing)

---

## Task Structure 📋

Each task has the following properties:

| Property      | Description                                |
|---------------|--------------------------------------------|
| `id`          | Unique identifier (auto-generated)         |
| `description` | Short description of the task              |
| `status`      | `todo`, `in-progress`, or `done`           |
| `createdAt`   | Timestamp when task was created            |
| `updatedAt`   | Timestamp of last update                   |

---

## Installation 💻

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd task-tracker-cli
2.Verify Python 3 is installed:
  python --version
  
**Usage**
# Add a task
python task_cli.py add "Buy groceries"

# Update a task
python task_cli.py update 1 "Buy groceries and cook dinner"

# Delete a task
python task_cli.py delete 1

# Mark as in-progress
python task_cli.py mark-in-progress 1

# Mark as done
python task_cli.py mark-done 1

# List all tasks
python task_cli.py list

# Filter by status
python task_cli.py list todo
python task_cli.py list in-progress
python task_cli.py list done

JSON Storage 🗂️
Tasks saved in tasks.json in project directory

Auto-created if file doesn't exist

Real-time updates - changes saved immediately

Error Handling ⚠️
❌ Invalid task IDs → Clear error message

📄 Missing/empty JSON → Gracefully handled

🔢 Duplicate IDs → Auto-generated unique IDs

Development Guide 🛠️
Step 1: Project Initialization
bash
mkdir task-tracker-cli
cd task-tracker-cli
git init
touch task_cli.py tasks.json
Step 2: Feature Implementation Order
Add Task → Create with ID, description, timestamps

List Tasks → All tasks + status filters

Update Task → Edit description, update updatedAt

Delete Task → Remove by ID

Mark Status → in-progress / done

CLI Interface → argparse for commands

Step 3: Testing Checklist
 Add task → Verify JSON structure

 Invalid ID → Proper error handling

 Empty list → Shows "No tasks found"

 Status filtering → Correct results

Future Improvements ✨
🎯 Task priorities (low, medium, high)

📅 Due dates & reminders

📊 Export to CSV/PDF

🎮 Interactive menu mode

🏷️ Categories/tags

🔍 Search functionality
