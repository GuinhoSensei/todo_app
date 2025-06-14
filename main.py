from models import *

def menu():
    print("\n=== To-Do Manager ===")
    print("1. Create User")
    print("2. Add Task for User")
    print("3. View User's Tasks")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Exit")

while True:
    menu()
    choice = input("Choose an option: ")

    if choice == "1":
        username = input("Username: ")
        email = input("Email: ")
        create_user(username, email)
        print("User created!")

    elif choice == "2":
        username = input("Username: ")
        user = get_user_by_username(username)
        if user:
            title = input("Task Title: ")
            due = input("Due Date (YYYY-MM-DD): ")
            create_task(user["_id"], title, due)
            print("Task added.")
        else:
            print("User not found.")

    elif choice == "3":
        username = input("Username: ")
        user = get_user_by_username(username)
        if user:
            tasks = get_tasks_for_user(user["_id"])
            if not tasks:
                print("No tasks found.")
            for task in tasks:
                print(f"{task['_id']} - {task['title']} (Due: {task['due_date']})")
        else:
            print("User not found.")

    elif choice == "4":
        task_id = input("Task ID to update: ")
        new_title = input("New title: ")
        update_task(task_id, new_title)
        print("Task updated.")

    elif choice == "5":
        task_id = input("Task ID to delete: ")
        delete_task(task_id)
        print("Task deleted.")

    elif choice == "6":
        print("Goodbye!")
        break
