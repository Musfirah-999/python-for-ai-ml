
def takeInput(to_do_list):
   add = input("Enter the task to add:")
   to_do_list.append(add)

def removeTask(to_do_list):
    rem = input("Enter the task to remove:")
    if rem in to_do_list:
        to_do_list.remove(rem)
    else:
        print("Task not found in the list.")

def viewTasks(to_do_list):
    if not to_do_list:
        print("No tasks in the to-do list.")
    else:
        print("------To-Do List------")
        for idx, task in enumerate(to_do_list, start=1):
            print(f"{idx}. {task}")
def showList(): 
        print("------To-Do List Options------")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        
def main():
    to_do_list = []
    while True:
        showList()
        user_option = input("Choose an option (1-4): ")
        if user_option =="1":
            takeInput(to_do_list)
        elif user_option == "2":
            removeTask(to_do_list)
        elif user_option == "3":
            viewTasks(to_do_list)
        elif user_option == "4":
            print("Exiting To-Do List.")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 4.")
main()