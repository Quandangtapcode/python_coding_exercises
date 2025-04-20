import requests

API_URL = "http://localhost:5000/api/tasks"

def get_tasks():
    response = requests.get(API_URL)
    tasks = response.json()
    print("\n===List tasks===")
    for task in tasks:
        status = "done" if task['status'] else "unfinished"
        print(f"[{task['id']}] {task['title']} - Deadline: {task['deadline']} - Status: {status}")
        print("") 

def add_task():
    title = input("Enter the name task:")
    deadline = input("Enter deadline (YYYY-MM-DD):")
    response = requests.post(API_URL, json ={"title": title, "deadline": deadline})
    print(response.json()["message"])
    
    
def update_task():
    task_id = input("Enter ID task need to update:")
    title = input("New title:")
    deadline = input("New deadline(YYYY-MM-DD):")
    status = int(input("Status (1:Done, 0:Unfinished): "))
    response = requests.put(f"{API_URL}/{task_id}", json={
        "title": title,
        "deadline": deadline,
        "status": status
    })
    print(response.json()["message"])
    

def check_task_status():
    task_id = input("Enter ID task need to check: ")
    response = requests.put(f"{API_URL}/{task_id}/complete")
    
    if response.status_code == 200:
        print(response.json().get("message"))
    else:
        print(f"Error: Task with ID {task_id} not found.")    
    
    
    
    
def delete_task_by_id():
    task_id = input("Enter ID task need to deleted:")
    response = requests.delete(f"{API_URL}/{task_id}")
    print(response.json()["message"])
    
    
    
def delete_all_tasks():
    confirm = input("Are you sure you want to delete all the tasks? (yes/no):")
    if confirm.lower() == 'yes':
        response = requests.delete(API_URL)
        print(response.json()["message"])
    else:
        print("Cancel manipulation.")            
        

def main():
    while True:
        print("""
======== TO-DO LIST APP =========
1. List tasks
2. Add task
3. Update task
4. Check status task
5. Delete task by id
6. Delete all tasks
7. Exit
""")
        choice = input("Select : ")
        if choice == '1':
            get_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            check_task_status()    
        elif choice == '5':
            delete_task_by_id()
        elif choice == '6':
            delete_all_tasks()
        elif choice == '7':
            print("Exit.") 
            break
        else:
            print("Invalid select.")

if __name__ == "__main__":
    main()
