# Empty list to store tasks
tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("No tasks in your list.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

while True:
    print("\n--- TO DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        show_tasks()
        try:
            num = int(input("Enter task number to remove: "))
            removed = tasks.pop(num - 1)
            print(f"Removed: {removed}")
        except:
            print("Invalid input!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
