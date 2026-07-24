# todo_app.py

tasks = []

while True:
    print("\nTodo App")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        task = input("Enter task: ")
        tasks.append(task)
        print("Task Added!")

    elif choice == 2:
        print("\nYour Tasks")
        if len(tasks) == 0:
            print("No tasks.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(i, ".", task)

    elif choice == 3:
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(i, ".", task)

            index = int(input("Enter task number: "))
            tasks.pop(index - 1)
            print("Task Removed!")

    elif choice == 4:
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")