tasks = []

def add_task():
    """Function to add a new task to the list."""
    while True:
        task = input("Add task (or type 'e' to exit): ").strip()
        if task.lower() == 'e':
            break

        if task in tasks:
            print("Item already exists.")
        else:
            tasks.append(task)
            print("Task added.")
            print(tasks)

def edit_task():
    """Function to edit an existing task in the list."""
    if not tasks:
        print("No tasks to edit.")
        return

    print("Current tasks:")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task}")

    while True:
        try:
            task_index = int(input("Enter the number of the task you want to edit (or enter 0 to cancel): ")) - 1
            if task_index == -1:
                break

            if 0 <= task_index < len(tasks):
                new_task = input("Enter the new task: ").strip()
                if new_task in tasks:
                    print("Item already exists.")
                else:
                    tasks[task_index] = new_task
                    print("Task updated.")
                    print(tasks)
                break
            else:
                print("Invalid task number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    
    while True:
        action = input("What would you like to do? (a)dd, (e)dit, or (q)uit: ").strip().lower()

        if action == 'a':
            add_task()
        elif action == 'e':
            edit_task()
        elif action == 'q':
            break
        else:
            print("Invalid choice. Please enter 'a', 'e', or 'q'.")

if __name__ == "__main__":
    main()
