#To-Do-List Application

tasks = []

def show_menu():
    print("\n---TO-DO LIST---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Remove Task")
    print("5. Exit")


def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "done": False})
    print(f"Task '{task}' added successfully!")


def view_tasks():
    if not tasks:
        print("No tasks yet!")
        return
    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Pending"
        print(f"{index}. {task['task']} [{status}]")


def mark_done():
    view_tasks()
    if not tasks:
        return
    try:
        index = int(input("Enter the task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("Marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def remove_task():
    view_tasks()
    if not tasks:
        return
    try:
        index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Removed task: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        remove_task()
    elif choice == '5':
        print("Exiting the To-Do List. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")


