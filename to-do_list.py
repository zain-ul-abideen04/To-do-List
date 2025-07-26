def show_menu():
    print("\n--- Welcome to To-Do List ---")
    print("Press 1 to add a task")
    print("Press 2 to view tasks")
    print("Press 3 to delete a task")
    print("Press 4 to exit")

def add_task(task_list):
    task = input("Enter a task: ")
    task_list.append(task)
    print("Task added!")

def view_task(task_list):
    if not task_list:
        print("No tasks added yet.")
    else:
        print("\n Your Tasks:")
        for i, task in enumerate(task_list, start=1):
            print(f"{i}. {task}")

def delete_task(task_list):
    view_task(task_list)
    try:
        num = int(input("Enter the number of the task to remove: "))
        if 1 <= num <= len(task_list):
            removed = task_list.pop(num - 1)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

task = []

while True:
    show_menu()
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_task(task)
        elif choice == 2:
            view_task(task)
        elif choice == 3:
            delete_task(task)
        elif choice == 4:
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid input. Choose between 1-4.")
    except ValueError:
        print("Please enter a number only.")
