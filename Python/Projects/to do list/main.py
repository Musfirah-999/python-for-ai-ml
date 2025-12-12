import json
file_name = "todo_list.json"

def load_tasks():
  try:
    with open(file_name, "r") as file:
        return json.load(file)
  except:
      return {"tasks": []}

def view_tasks():
    pass

def save_tasks(tasks):
 try:
    with open(file_name, "w") as file:
        json.dump(tasks,file)  #save task
 except:
      print("Failed to save!!")   

def create_tasks(tasks):
    description = input("Enter the task description:").strip()
    if description:
        tasks["tasks"].append({"description": description, "complete": False})
        save_tasks(tasks)
        print("Task added")
    else:
       print("Description cannot be empty.") 

def mark_tasks_completed():
    pass


def main():
    tasks = load_tasks()
    
    while True:
        print("\nTO-DO-LIST-MANAGER")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Exit")
        
        choice = input("Enter your choice:").strip()
        if choice == "1":
            view_tasks()
        elif choice == "2":
            create_tasks(tasks)
            
        elif choice == "3":
            mark_tasks_completed()
        elif choice == "4":
            print("Good bye!!")
            break
        else:
            print("Invalid choice. Please try again.")

main()