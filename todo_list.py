def main():
    print("Welcome to todolist")
    print("Choose your option:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Complete task")
    
    print("4. Delete task")
    print("5. Quit")

    tasks = []

    while True:
        user_choice = input("Enter your choice:\n ")

        if user_choice == "1":
            add_task(tasks)
        elif user_choice == "2":
            view_tasks(tasks)
        elif user_choice == "3":
            complete_task(tasks)
        elif user_choice == "4":
            delete_task(tasks)
        elif user_choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added.\n")

def view_tasks(tasks):
    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Not completed"
        print(f"{i}. {task['task']} - {status}\n")

def complete_task(tasks):
    task_number = int(input("Enter the task number to complete: ")) - 1
    if task_number < len(tasks):
        tasks[task_number]["completed"] = True
        print(f"Task {task_number + 1} completed.\n")
    else:
        print("Invalid task number.\n")

def delete_task(tasks):
    task_number = int(input("Enter the task number to delete: ")) - 1
    if task_number < len(tasks):
        del tasks[task_number]
        print(f"Task {task_number + 1} deleted.\n")
    else:
        print("Invalid task number.\n")

if __name__ == "__main__":
    main()