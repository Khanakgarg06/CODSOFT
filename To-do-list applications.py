tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        print("\nYour Tasks:")

        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for index, task in enumerate(tasks, start=1):
                print(index, ".", task)

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")

        else:
            for index, task in enumerate(tasks, start=1):
                print(index, ".", task)

            task_num = int(input("Enter task number to delete: "))

            if 1 <= task_num <= len(tasks):
                tasks.pop(task_num - 1)
                print("Task deleted successfully!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Thank you for using the To-Do List App!")
        break

    else:
        print("Invalid choice. Please try again.")