#!/usr/bin/env python3
"""
app.py — Simple To-Do CLI App

Features:
- Add tasks
- View tasks
- Delete tasks
- Quit

Storage: in-memory Python list
Error handling: try/except/else/finally around user interactions
"""

from typing import List


def print_banner() -> None:
    """Display a welcome banner."""
    print("=" * 50)
    print("📝  Welcome to the To-Do CLI")
    print("=" * 50)


def show_menu() -> None:
    """Display the main menu options."""
    print("\nPlease choose an option:")
    print("1) Add task")
    print("2) View tasks")
    print("3) Delete task")
    print("4) Quit")


def prompt_continue() -> None:
    """Pause so the user can read messages before the next screen."""
    input("\nPress Enter to continue...")


def add_task(tasks: List[str]) -> None:
    """
    Add a task to the list with input validation and error handling.
    Uses try/except/else/finally to demonstrate robust flow.
    """
    print("\n➕ Add a Task")
    try:
        task = input("Enter task description: ").strip()
        if not task:
            raise ValueError("Task cannot be empty.")
        tasks.append(task)
    except ValueError as e:
        print(f"⚠️  Invalid input: {e}")
    else:
        print(f"✅ Task added: '{task}'")
    finally:
        prompt_continue()


def view_tasks(tasks: List[str]) -> None:
    """
    Display all tasks. Alerts the user if there are no tasks to view.
    Demonstrates else/finally in a non-exception path as well.
    """
    print("\n👀 View Tasks")
    try:
        if not tasks:
            raise LookupError("There are no tasks to view.")
    except LookupError as e:
        print(f"ℹ️  {e}")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    finally:
        prompt_continue()


def delete_task(tasks: List[str]) -> None:
    """
    Delete a task by its number with robust validation.
    Alerts if the task number doesn't exist or input is invalid.
    """
    print("\n🗑️  Delete a Task")
    try:
        if not tasks:
            raise LookupError("There are no tasks to delete.")
        # Show tasks before asking which to delete
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

        raw = input("Enter the number of the task to delete: ").strip()
        if not raw:
            raise ValueError("You must enter a task number.")
        number = int(raw)  # may raise ValueError

        if number < 1 or number > len(tasks):
            raise IndexError(f"Task #{number} does not exist.")
        removed = tasks.pop(number - 1)
    except ValueError:
        print("⚠️  Invalid input: please enter a whole number (e.g., 1, 2, 3).")
    except LookupError as e:
        print(f"ℹ️  {e}")
    except IndexError as e:
        print(f"⚠️  {e}")
    else:
        print(f"✅ Deleted task: '{removed}'")
    finally:
        prompt_continue()


def get_choice() -> int:
    """
    Prompt the user for a menu choice (1-4).
    Returns a valid integer; otherwise raises ValueError.
    """
    raw = input("Enter choice (1-4): ").strip()
    choice = int(raw)  # may raise ValueError
    if choice not in (1, 2, 3, 4):
        raise ValueError("Menu option does not exist.")
    return choice


def run() -> None:
    """Main application loop."""
    tasks: List[str] = []
    print_banner()

    while True:
        show_menu()
        try:
            choice = get_choice()
        except ValueError as e:
            # Covers invalid numbers, non-numeric input, and out-of-range choices
            print(f"⚠️  Invalid selection: {e}")
            prompt_continue()
            continue

        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            view_tasks(tasks)
        elif choice == 3:
            delete_task(tasks)
        elif choice == 4:
            try:
                print("\n👋 Thanks for using the To-Do CLI. Goodbye!")
            finally:
                break


if __name__ == "__main__":
    run()
