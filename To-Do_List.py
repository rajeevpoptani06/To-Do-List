import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file if it exists."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(FILE_NAME, 'w') as file:
        json.dump(tasks, file, indent=4)

def view_tasks(tasks):
    """Display all current tasks."""
    print("\n--- Your To-Do List ---")
    if not tasks:
        print("No tasks found. Enjoy your day! ✨")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    print("--------------------------")

def add_task(tasks):
    """Add a new task to the list."""
    task = input("Enter the new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f"Task added: '{task}'")
    else:
        print("Task cannot be empty!")

def delete_task(tasks):
    """Delete a task by its number."""
    view_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("\nEnter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task deleted: '{removed_task}'")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    """Main menu loop for the CLI app."""
    tasks = load_tasks()
    
    while True:
        print("\n--- Main Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Select an option (1-4): ").strip()

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("Goodbye! Keep crushing your goals! 🚀")
            break
        else:
            print("Invalid choice! Please select between 1 and 4.")

if __name__ == "__main__":
    main()