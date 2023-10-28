class TaskList():
    def __init__(self):
        self.tasklist = []


    def print_list(self):
        for i in enumerate(self.tasklist, start=1):
            print(f"{i}.{self.tasklist}")

    def add_task(self,tasks):
        self.tasklist.append(tasks)

    def delete_task(self, task):
        self.tasklist.remove(task)

    def complete_tasks(self, task):
        completed_list = []
        completed_list.append(task)
        for i in enumerate(completed_list, start=1):
            print("These tasks are completed \n",i,completed_list)

        updated_list = list(set(self.tasklist) - set(completed_list))
        for i in enumerate(updated_list, start=1):
            print("The updated list is \n",i,updated_list)



list1 = TaskList()
list1.add_task("clean room")
list1.add_task("read book")
list1.print_list()

list1.delete_task("clean room")
list1.print_list()

list1.complete_tasks("read book")