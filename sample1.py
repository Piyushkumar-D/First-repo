import datetime

tasks = []

def show_menu():
    print("\n===== My To-Do List =====")
    print("1 - View Tasks")
    print("2 - Add Task")
    print("3 - Remove Task")
    print("4 - Clear All Tasks")  # new feature
    print("5 - Exit")
    print("=========================")

def view_tasks():
    if not tasks:
        print("📝 No tasks yet! Add one using option 2.")
    else:
        print("\n-- Your Tasks --")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['task']} (added on {task['time']})")

def add_task():
    task_text = input("Enter a new task: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tasks.append({"task": task_text, "time": timestamp})
    print(f"✅ Task '{task_text}' added successfully at {timestamp}!")

def remove_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to remove: "))
        removed = tasks.pop(task_no - 1)
        print(f"🗑️ Removed task: {removed['task']}")
    except (ValueError, IndexError):
        print("⚠️ Invalid input! Please try again.")

def clear_tasks():
    confirm = input("Are you sure you want to clear all tasks? (y/n): ").lower()
    if confirm == "y":
        tasks.clear()
        print("🧹 All tasks have been cleared!")
    else:
        print("❎ Clear all cancelled.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            clear_tasks()
        elif choice == "5":
            print("👋 Exiting To-Do App. Goodbye!")
            break
        else:
            print("❌ Invalid option! Please try again.")

if __name__ == "__main__":
    main()
# This line was added from Feature1 branch
