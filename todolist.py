tasks = []
last_action = None

def add_task():
    """Function to add a new task to the list."""
    global last_action
    while True:
        task = input("Add task (or type 'e' to exit): ").strip()
        if task.lower() == 'e':
            break

        if any(t['name'] == task for t in tasks):
            print("Item already exists.")
        else:
            tasks.append({"name": task, "completed": False})
            last_action = ('add', len(tasks) - 1, None)  # Store the add action for undo
            print("Task added.")
            print_tasks()

def print_tasks():
    """Function to display the current tasks."""
    if not tasks:
        print("No tasks available.")
    else:
        print("Current tasks:")
        for i, task in enumerate(tasks):
            status = "✓" if task["completed"] else "✗"
            # ANSI escape codes for green and red colors
            status_color = "\033[92m" if task["completed"] else "\033[91m"
            # Reset color
            reset_color = "\033[0m"
            print(f"{i + 1}. {task['name']} [{status_color}{status}{reset_color}]")

def edit_task():
    """Function to edit an existing task in the list."""
    global last_action
    if not tasks:
        print("No tasks to edit.")
        return

    print_tasks()

    while True:
        try:
            task_index = int(input("Enter the number of the task you want to edit (or enter 0 to cancel): ")) - 1
            if task_index == -1:
                break

            if 0 <= task_index < len(tasks):
                old_task = tasks[task_index]["name"]
                new_task = input("Enter the new task: ").strip()
                if any(t['name'] == new_task for t in tasks):
                    print("Item already exists.")
                else:
                    tasks[task_index]["name"] = new_task
                    last_action = ('edit', task_index, old_task)  # Store the edit action for undo
                    print("Task updated.")
                    print_tasks()
                break
            else:
                print("Invalid task number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def mark_task_completed():
    """Function to mark a task as completed."""
    global last_action
    if not tasks:
        print("No tasks to mark as completed.")
        return

    print_tasks()

    while True:
        try:
            task_index = int(input("Enter the number of the task you want to mark as completed (or enter 0 to cancel): ")) - 1
            if task_index == -1:
                break

            if 0 <= task_index < len(tasks):
                last_action = ('mark_complete', task_index, tasks[task_index]["completed"])  # Store the mark complete action for undo
                tasks[task_index]["completed"] = True
                print(f"Task '{tasks[task_index]['name']}' marked as completed.")
                print_tasks()
                break
            else:
                print("Invalid task number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def delete_task():
    """Function to delete a task from the list."""
    global last_action
    if not tasks:
        print("No tasks to delete.")
        return

    print_tasks()

    while True:
        try:
            task_index = int(input("Enter the number of the task you want to delete (or enter 0 to cancel): ")) - 1
            if task_index == -1:
                break

            if 0 <= task_index < len(tasks):
                deleted_task = tasks.pop(task_index)
                last_action = ('delete', task_index, deleted_task)  # Store the delete action for undo
                print(f"Task '{deleted_task['name']}' has been deleted.")
                print_tasks()
                break
            else:
                print("Invalid task number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def undo_action():
    """Function to undo the last action performed."""
    global last_action
    if not last_action:
        print("No action to undo.")
        return

    action, task_index, task_data = last_action

    if action == 'add':
        tasks.pop(task_index)
        print("Undo: Last task added has been removed.")
    elif action == 'edit':
        tasks[task_index]["name"] = task_data
        print("Undo: Last task edit has been reverted.")
    elif action == 'mark_complete':
        tasks[task_index]["completed"] = task_data
        print("Undo: Last task completion has been reverted.")
    elif action == 'delete':
        tasks.insert(task_index, task_data)
        print(f"Undo: Task '{task_data['name']}' has been restored.")

    last_action = None  # Clear the last action after undoing
    print_tasks()

def main():
    """Main function to control the flow of the program."""
    while True:
        action = input("What would you like to do? (a)dd, (e)dit, (m)ark as completed, (d)elete, (u)ndo, or (q)uit: ").strip().lower()

        if action == 'a':
            add_task()
        elif action == 'e':
            edit_task()
        elif action == 'm':
            mark_task_completed()
        elif action == 'd':
            delete_task()
        elif action == 'u':
            undo_action()
        elif action == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 'a', 'e', 'm', 'd', 'u', or 'q'.")

if __name__ == "__main__":
    main()
