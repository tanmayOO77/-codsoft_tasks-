"""
CodSoft Internship - Task 1: To-Do List Manager
-------------------------------------------------
A command-line to-do list application with persistent JSON storage.
Add, view, mark as done, and delete tasks.
"""

import json
import os

DATA_FILE = "tasks.json"


def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def display_tasks(tasks):
    if not tasks:
        print("\n📋 No tasks yet. Add one!\n")
        return

    print("\n" + "=" * 45)
    print(" 📋  YOUR TO-DO LIST")
    print("=" * 45)
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"  {i}. {status}  {task['title']}")
    print("=" * 45)

    done_count = sum(1 for t in tasks if t["done"])
    print(f"  Progress: {done_count}/{len(tasks)} completed\n")


def add_task(tasks):
    title = input("Enter task description: ").strip()
    if not title:
        print("❌ Task description cannot be empty.\n")
        return
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"✅ Task added: {title}\n")


def mark_done(tasks):
    if not tasks:
        print("❌ No tasks to mark.\n")
        return

    display_tasks(tasks)
    raw = input("Enter task number to mark as done: ").strip()

    if not raw.isdigit():
        print("❌ Please enter a valid number.\n")
        return

    index = int(raw) - 1
    if index < 0 or index >= len(tasks):
        print("❌ Invalid task number.\n")
        return

    tasks[index]["done"] = True
    save_tasks(tasks)
    print(f"✅ Marked as done: {tasks[index]['title']}\n")


def delete_task(tasks):
    if not tasks:
        print("❌ No tasks to delete.\n")
        return

    display_tasks(tasks)
    raw = input("Enter task number to delete: ").strip()

    if not raw.isdigit():
        print("❌ Please enter a valid number.\n")
        return

    index = int(raw) - 1
    if index < 0 or index >= len(tasks):
        print("❌ Invalid task number.\n")
        return

    removed = tasks.pop(index)
    save_tasks(tasks)
    print(f"🗑️  Deleted: {removed['title']}\n")


def main():
    print("=" * 45)
    print(" CodSoft — To-Do List Manager")
    print("=" * 45)

    tasks = load_tasks()

    while True:
        print("  1. View Tasks")
        print("  2. Add Task")
        print("  3. Mark Task as Done")
        print("  4. Delete Task")
        print("  5. Exit")

        choice = input("\nChoose an option (1-5): ").strip()

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("\n👋 Goodbye!\n")
            break
        else:
            print("❌ Invalid option. Try again.\n")


if __name__ == "__main__":
    main()
