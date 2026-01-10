# First, let’s create a Task class
class Task:
    def __init__(self, name):
        self.name = name
        self.is_done = False

# Now, create a To-Do List class that manages tasks
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        new_task = Task(task_name)
        self.tasks.append(new_task)
        print(f"Task '{task_name}' has been added!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks yet.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                status = "Done" if task.is_done else "Not done"
                print(f"{index}. {task.name} - {status}")

    def mark_done(self, task_index):
        if 0 <= task_index - 1 < len(self.tasks):
            self.tasks[task_index - 1].is_done = True
            print(f"Task number {task_index} has been marked as done!")
        else:
            print("Oops! Enter a valid task number.")

# Now let’s start the fun part
def main():
    todo_list = ToDoList()

    while True:
        print("\nWhat would you like to do?")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Mark a task as done")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Enter the task name: ")
            todo_list.add_task(task_name)

        elif choice == "2":
            todo_list.view_tasks()

        elif choice == "3":
            try:
                task_index = int(input("Enter the task number to mark as done: "))
                todo_list.mark_done(task_index)
            except ValueError:
                print("Please enter a valid number!")

        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Please choose a valid option.")

# This line starts the program
if __name__ == "__main__":
    main()
