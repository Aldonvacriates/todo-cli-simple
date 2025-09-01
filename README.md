# 📝 To-Do CLI App

A beginner-friendly **Command Line Interface (CLI)** To-Do application written in Python.  
This version stores tasks only in memory (using a Python list) and demonstrates core programming concepts like input handling, error handling, and functions.

---

## ✨ Features

- ➕ Add tasks
- 👀 View tasks
- 🗑️ Delete tasks
- 🚪 Quit the application
- ⚠️ Input validation with helpful error messages
- 🛡️ Error handling using `try`, `except`, `else`, and `finally`

---

## 📦 Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Aldonvacriates/todo-cli-simple.git
   cd todo-cli-simple
Run the app:

bash

python app.py
🐍 Requires Python 3.8 or higher.

🎮 Usage
When you run the app, you’ll see a simple menu:


📝  Welcome to the To-Do CLI
==================================================

Please choose an option:
1) Add task
2) View tasks
3) Delete task
4) Quit
Example Workflow
Add Task


Copy code
➕ Add a Task
Enter task description: Finish homework
✅ Task added: 'Finish homework'
View Tasks



👀 View Tasks
1. Finish homework
Delete Task


🗑️  Delete a Task
1. Finish homework
Enter the number of the task to delete: 1
✅ Deleted task: 'Finish homework'
Quit


👋 Thanks for using the To-Do CLI. Goodbye!
🧪 Testing Ideas
Try adding an empty task → should show an error

Try viewing tasks when none exist → should show a helpful alert

Try deleting a non-existent task number → should warn you

Try entering letters instead of numbers in the menu → should handle gracefully

🎯 Learning Goals
This project demonstrates:

Writing and organizing Python functions

Building a simple text-based user interface

Using lists to store data

Input validation and error handling with try/except/else/finally

📜 License
This project is licensed under the MIT License.