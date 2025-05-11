def task():
    tasks = []
    print("----- WELCOME TO THE TASK MANAGEMENT APP -----")

    try:
        total_task = int(input("Enter how many tasks you want to add: "))
    except ValueError:
        print("Invalid number.")
        return

    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)

    print(f"\nToday's tasks:\n{tasks}")

    while True:
        try:
            operation = int(input("Enter:\n1 - Add\n2 - Update\n3 - Delete\n4 - View\n5 - Exit\nYour choice: "))
        except ValueError:
            print("Invalid input. Enter a number from 1 to 5.")
            continue

        if operation == 1:
            add = input("Enter task to add: ")
            tasks.append(add)
            print(f"Task '{add}' added successfully.")

        elif operation == 2:
            updated_val = input("Enter the task name to update: ")
            if updated_val in tasks:
                new_task = input("Enter new task: ")
                index = tasks.index(updated_val)
                tasks[index] = new_task
                print(f"Task updated to '{new_task}'.")
            else:
                print("Task not found.")

        elif operation == 3:
            del_val = input("Enter the task to delete: ")
            if del_val in tasks:
                tasks.remove(del_val)
                print(f"Task '{del_val}' has been deleted.")
            else:
                print("Task not found.")

        elif operation == 4:
            print("\nCurrent Tasks:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")

        elif operation == 5:
            print("Closing the program. Goodbye!")
            break

        else:
            print("Invalid Input. Please select from 1 to 5.")

task()

