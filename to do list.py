todo_list = []

while True:
    print("\n--- TO DO LIST ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter task: ")
        todo_list.append(task)
        print("Task added.")

    elif choice == "2":
        if len(todo_list) == 0:
            print("No tasks in the list.")
        else:
            print("\nYour Tasks:")
            for i in range(len(todo_list)):
                print(i + 1, ".", todo_list[i])

    elif choice == "3":
        if len(todo_list) == 0:
            print("No tasks to remove.")
        else:
            task_no = int(input("Enter task number to remove: "))
            todo_list.pop(task_no - 1)
            print("Task removed.")

    elif choice == "4":
        print("Exiting To-Do List. Bye!")
        break

    else:
        print("Invalid choice. Try again.")
