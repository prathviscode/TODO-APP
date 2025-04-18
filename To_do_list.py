import json

def load_tasks_from_file():
    global Tasks
    with open("C:/Users/prrj7/OneDrive/Desktop/python/Projects/TODO App/my_task.json", "r") as f:
        Tasks = json.load(f)

def save_task_to_file():
    with open("C:/Users/prrj7/OneDrive/Desktop/python/Projects/TODO App/my_task.json", "w") as f:
        json.dump(Tasks, f, indent=4)

Tasks = []
def main():
    load_tasks_from_file()
    print("====== To-Do List ======")
    while True:
        print("""
            1. Add Task
            2. Show Tasks
            3. Marks Task as Done
            4. Remove Task
            5. Exit""")
        choise = int(input("Enter your choise: "))

        if choise == 1:
            n_task = int(input("How many task you want to add: "))
            for i in range(n_task):
                task = input("Enter your task: ")
                Tasks.append({"task":task, "done":False})
                print("task added!")

            save_task_to_file()


        elif choise == 2:
            print("\nTasks: ")
            for Index, task in enumerate(Tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{Index+1}. {task['task']} - {status}")

        elif choise == 3:
            mark = int(input("Enter the task number to marks as done: "))-1
            if mark >= 0 and mark < len(Tasks):
                Tasks[mark]["done"] = True
                save_task_to_file()
                print("Task marks as Done!")
            else:
                print("Invalid task number.")

        elif choise == 4:
            print("""
            1. Remove one by one: 
            2. Remove all at once: """)
            op = int(input("Select Option: "))
            if op == 1:
                r_task = int(input("Enter the task number to remove: "))-1
                if r_task >= 0 and r_task < len(Tasks):
                    Tasks.pop(r_task)
                    save_task_to_file()
                    print("Task removed!")

            elif op == 2:
                Tasks.clear()
                print("all tasks are removed!")
                save_task_to_file()

            else:
                print("Invalid task number.")



        elif choise == 5:
            print("Exit the todo app: ")
            break
        else:
            print("Invalid choise Please try again")

main()
