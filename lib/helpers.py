from db.models import User, ToDo, Category, DueDate, session
from datetime import datetime
from getpass import getpass
from quote import quote
from py_random_words import RandomWords

random_word = RandomWords()
w = random_word.get_word()
result = quote(w, limit=1)



def exit_program():
    print("----------------------------------------------------")
    print(result[0]['quote'])
    print("************************************")
    print(f"Quote by -> {result[0]['author']}")
    print("************************************")
    exit()

def login():
    from cli import sub_main
    try:
        # Retrieve existing users from the databse
        users = session.query(User).all()
        if not users:
            print("No users found. Please create a user first.")
            return
        print("----------------------------------------------------")
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

        # Validate the password
        if user.password == password:
            print("You have successfully logged in!")
            sub_main(user)    
        else:
            print("Incorrect password.")
    except Exception as exc:
        print("Error logging in: ", exc)

def add_todo(user):
    try:
        task = input("Enter the task: ")
        category_name = input("Enter the category: ")
        due_date_str = input("Enter the due date (YYYY-MM-DD HH:MM:SS): ")

        # Retrieve category and due date objects based on input values 
        category = session.query(Category).filter_by(name=category_name).first()
        due_date = DueDate(date=datetime.strptime(due_date_str, "%Y-%m-%d %H:%M:%S"))

        todo = user.create_todo(task, category, due_date)
        print(f'Success: <{task}> added to your todos!')
    except Exception as exc:
        print("Error adding todo: ", exc)

def remove_todo(user):
    try:
        # Get all todos for the user from the database
        todos = session.query(ToDo).filter_by(user_name=user.username).all()

        # Check if there are any todos for the user
        if not todos:
            print("You have no todos")
            return
        
        print("----------------------------------------------------")      
        # Print the list of todos with their IDs
        print("Your todos:")
        for todo in todos:
            print("******")
            print(f"ID: {todo.id_} //-> Todo: {todo.task} //-> DueDate: {todo.due_date_date}")

        # Prompt teh user to enter the ID of the todo they want to delete
        delete_id = int(input("Enter the ID of the todo to delete: "))

        # Call the delete_todo function to delete the selscted todo
        user.delete_todo(delete_id)

        print(f"Success: Todo deleted!")
    except Exception as exc:
        print("Error removing todo: ", exc)


def change_username(user):
    try:
        print("----------------------------------------------------")         
        new_username = input("Enter the new username: ")
        user.update_username(new_username)
        print(f"Success: Username updated to {new_username}")
    except Exception as exc:
        print("Error changing username: ", exc)

def all_todos(user):
    try:
        # Get all todos for the user from the database
        todos = user.get_todos()

        # Check if there are any todos for the user
        if not todos:
            print("You have no todos")
            return
        
        print("----------------------------------------------------")      
        # Print the list of todos with their IDs
        print("Your todos sorted by date:")
        for todo in todos:
            print("******")
            print(f"//-> Todo: {todo.task} //-> DueDate: {todo.due_date_date}")
    except Exception as exc:
        print("Error getting todos: ", exc)