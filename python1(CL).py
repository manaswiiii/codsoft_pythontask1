# to do list

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                status = "Completed" if task["completed"] else "Not Completed"
                print(f"{index}. {task['task']} - {status}")

    def mark_task_completed(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            del self.tasks[task_number - 1]
        else:
            print("Invalid task number.")

    def run(self):
        while True:
            print("\nTo-Do List Application")
            print("1. Add a task")
            print("2. View all tasks")
            print("3. Mark a task as completed")
            print("4. Delete a task")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                task = input("Enter the task: ")
                self.add_task(task)
                print("Task added.")
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                task_number = int(input("Enter the task number to mark as completed: "))
                self.mark_task_completed(task_number)
                print("Task marked as completed.")
            elif choice == "4":
                task_number = int(input("Enter the task number to delete: "))
                self.delete_task(task_number)
                print("Task deleted.")
            elif choice == "5":
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    todo_list = TodoList()
    todo_list.run()
