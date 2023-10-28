task_list = []
completed_list = []

def add_task():
    while True:
        tasks = input("enter your tasks in list or exit to stop ").lower()
        if tasks == "exit":
            break
        else:
            task_list.append(tasks)
    return task_list

def delete_task(task_list):
    task = input("Enter the task you want to delete: ").lower()
    if task in task_list:
        task_list.remove(task)
        print(f"Task '{task}' has been deleted.")
    else:
        print("Task not found in the list.")

def complete_tasks(task_list,completed_list):
    task = input("Mark your complete tasks: ").lower()
    if task in task_list:
        task_list.remove(task)
        completed_list.append(task)
        print(f"Task '{task}' has been marked as completed.")
    else:
        print("Task not found in the list.")

def print_list(task_list):
    print("The tasks are:\n")
    for i in enumerate(task_list, start=1):
         print(f"{i}.{task_list}")



add_task()
while True:
    print_list(task_list)
    print("choice for following operations \n a: delete task \n b: complete task \n c: finish")
    choice = input("Enter your choice: \n ").lower()

    if choice == "a":
        delete_task(task_list)
    elif choice == "b":
        complete_tasks(task_list, completed_list)
    elif choice == "c":
        break
    else:
        print("Invalid choice. Please try again.")
