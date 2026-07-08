# To do list app using Gui
tasks = []


# for taking the input
def menu():
    print("\n---TO DO LIST---")
    print("1. Add task")
    print("2. View task")
    print("3. Mark as done")
    print("4. Delete Task")
    print("5. Exit")


#
def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "done": False})
    print(f"Task {tasks}added!")


#
def view_task():
    if not tasks:
        print("NO tasks yet! ")
        return
    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "❌"
        print(f"{index}.{task['task']}[{status}]")


#
def mark_done():
    view_task()
    if not tasks:
        return
    try:
        index = int(input("Enter the number to mark done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("Marked as done!")
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter  a vaid number. ")


#
def delete_task():
    view_task()
    if not tasks:
        return
    try:
        index = int(input("Enter the number to delete :")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Deleted task:{removed['task']}")
        else:
            print("invalid number!")

    except ValueError:
        print("Please enter the valid number.")


#
while True:
    menu()
    choice = input("Enter the number 1-5: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_task()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice Try again")
