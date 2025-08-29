text_file = "todo.txt"

def read_tasks():
    try:
        with open(text_file, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def write_tasks(tasks):
    with open(text_file, "w") as file:
        file.writelines(tasks)

while True:
    print("\n... Welcome To Todo Menu ...\n")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Mark task as complete")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks = read_tasks()
        tasks.append(f"[ ] {task}\n")
        write_tasks(tasks)
        print("Task added.")

    elif choice == "2":
        tasks = read_tasks()
        if tasks:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
        else:
            print("No tasks found.")

    elif choice == "3":
        tasks = read_tasks()
        if not tasks:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
            try:
                task_number = int(input("Enter the task number to remove: "))
                removed = tasks.pop(task_number - 1)
                write_tasks(tasks)
                print(f"Task '{removed.strip()}' removed.")
            except (ValueError, IndexError):
                print("Invalid task number.")

    elif choice == "4":
        tasks = read_tasks()
        if not tasks:
            print("No tasks to mark complete.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
            try:
                task_number = int(input("Enter the task number to mark complete: "))
                if 1 <= task_number <= len(tasks):
                    if tasks[task_number - 1].startswith("[ ]"):
                        tasks[task_number - 1] = tasks[task_number - 1].replace("[ ]", "[x]", 1)
                        write_tasks(tasks)
                        print("Task marked as complete.")
                    else:
                        print("Task already completed.")
                else:
                    print("Invalid task number.")
            except (ValueError, IndexError):
                print("Invalid task number.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
