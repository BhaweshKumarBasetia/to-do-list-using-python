class todolist:
    def __init__(self):
        self.task = []

    def add_task(self, task):
        self.task.append(task)
        print(f"Task '{task}' added.")

    def remove_task(self, task):
        if task in self.task:
            self.task.remove(task)
            print(f"Task '{task}' removed.")
        else:
            print(f"Task '{task}' not found.")

    def view_tasks(self):
        if self.task:
            print("To-Do List:")
            for idx, task in enumerate(self.task,1):
                print(f"{idx}. {task}")
        else:
            print("Your to-do list is empty.")
        
def main():
    todo_list = todolist()

    while True:
        print("\ntodo list Menu ")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. view a task")
        print("4. exit")

        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2' :
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()