from db.models import User, ToDo, Category, DueDate, session
from datetime import datetime
from getpass import getpass

def add_todo():
    # Retrieve existing users from the databse
    users = session.query(User).all()
    if not users:
        print("No users found. Please create a user first.")
        return
    
    # Prompt the user to select a user
    print("Select a user:")
    for index, user in enumerate(users):
        print(f"{index+1}. {user.username}")
    user_choice = input("Enter the user number: ")
    user_index = int(user_choice) - 1

    # Validate the user choice
    if user_index < 0 or user_index >= len(users):
        print("Invalid user selection.")
        return


    user = users[user_index]
    password = getpass("Enter your password: ")
    task = input("Enter the task: ")
    category_name = input("Enter the category: ")
    due_date_str = input("Enter the due date (YYYY-MM-DD HH:MM:SS): ")


    try:
        # Retrieve category and due date objects based on input values
        if user.password == password:
            category = session.query(Category).filter_by(name=category_name).first()
            due_date = DueDate(date=datetime.strptime(due_date_str, "%Y-%m-%d %H:%M:%S"))

            todo = user.create_todo(task, category, due_date)
            print(f'Success: <{task}> added to your todos!')
        else:
            print("Incorrect password.")
    except Exception as exc:
        print("Error creating todo: ", exc)

add_todo()
