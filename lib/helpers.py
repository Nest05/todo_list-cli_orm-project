from db.models import User, ToDo, Category, DueDate, session
from datetime import datetime
from getpass import getpass
from quote import quote
from py_random_words import RandomWords
import emoji
from colorama import init, Fore
init(autoreset=True)

random_word = RandomWords()
w = random_word.get_word()
result = quote(w, limit=1)



def exit_program():
    print(Fore.LIGHTMAGENTA_EX + "----------------------------------------------------")
    print("\U0001F4AD \U0001F4AC \U0001F4AD \U0001F4AC \U0001F4AD \U0001F4AC \U0001F914 \U0001F9D0")
    print(Fore.LIGHTWHITE_EX + result[0]['quote'])
    print(Fore.LIGHTMAGENTA_EX + "************************************")
    print(Fore.LIGHTRED_EX + f"Quote by -> {result[0]['author']}")
    print(Fore.LIGHTMAGENTA_EX + "************************************")
    exit()

def add_user():
    try: 
        print(Fore.LIGHTMAGENTA_EX + "----------------------------------------------------")
        print(Fore.LIGHTCYAN_EX + "Sign up here:")
        print(Fore.LIGHTMAGENTA_EX + "******")
        username = input("Enter your username: ")
        print(Fore.LIGHTMAGENTA_EX + "******")
        password = input("Enter your password: ")
        print(Fore.LIGHTMAGENTA_EX + "******")
        new_user = User(username=username, password=password)
        session.add(new_user)
        session.commit()

        print(Fore.GREEN + f"Welcome {username}! You signed up successfully!")
    except Exception as exc:
        print(Fore.RED + "An error occured in the signup process:", exc)

def login():
    from cli import sub_main
    try:
        # Retrieve existing users from the databse
        users = session.query(User).all()
        if not users:
            print(Fore.RED + "No users found. Please create a user first.")
            return
        print(Fore.LIGHTMAGENTA_EX + "----------------------------------------------------")
        # Prompt the user to select a user
        print(Fore.LIGHTCYAN_EX + "Select a user \U0001F642:")
        for index, user in enumerate(users):
            print(f"{index+1}. {user.username}")
        user_choice = input("Enter the user number: ")
        user_index = int(user_choice) - 1

        # Validate the user choice
        if user_index < 0 or user_index >= len(users):
            print(Fore.RED + "Invalid user selection.")
            return

        user = users[user_index]
        password = getpass("Enter your password \U0001F50F: ")

        # Validate the password
        if user.password == password:
            print(Fore.GREEN + "You have successfully logged in! \U0001F4AF")
            sub_main(user)    
        else:
            print(Fore.RED + "Incorrect password! \U0001F6AB \U0001FAE2")
    except Exception as exc:
        print(Fore.RED + "Error logging in: ", exc)

def add_todo(user):
    try:
        print(Fore.LIGHTMAGENTA_EX + "----------------------------------------------------")
        task = input("Enter the task: ")
        category_name = input("Enter the category: ")
        due_date_str = input("Enter the due date (YYYY-MM-DD HH:MM:SS): ")

        # Retrieve category and due date objects based on input values 
        category = session.query(Category).filter_by(name=category_name).first()
        due_date = DueDate(date=datetime.strptime(due_date_str, "%Y-%m-%d %H:%M:%S"))

        todo = user.create_todo(task, category, due_date)
        print(Fore.LIGHTGREEN_EX + f'Success: <{task}> added to your todos!')
    except Exception as exc:
        print(Fore.RED + "Error adding todo: ", exc)

def remove_todo(user):
    try:
        # Get all todos for the user from the database
        todos = session.query(ToDo).filter_by(user_name=user.username).all()

        # Check if there are any todos for the user
        if not todos:
            print(Fore.RED + "You have no todos")
            return
        
        print(Fore.LIGHTMAGENTA_EX + "----------------------------------------------------")      
        # Print the list of todos with their IDs
        print(Fore.BLUE + "Your todos \U0001F913:")
        for todo in todos:
            print(Fore.LIGHTMAGENTA_EX + "******")
            print(Fore.LIGHTWHITE_EX + f"ID: {todo.id_} //-> Todo: {todo.task} //-> DueDate \U000023F3: {todo.due_date_date}")

        # Prompt teh user to enter the ID of the todo they want to delete
        delete_id = int(input(Fore.RED + "[Warning: Once deleted it cannot be retrived!]Enter the ID of the todo to delete: "))

        # Call the delete_todo function to delete the selscted todo
        user.delete_todo(delete_id)

        print(Fore.LIGHTGREEN_EX + f"Success: Todo deleted!")
    except Exception as exc:
        print(Fore.RED + "Error removing todo: ", exc)


def change_username(user):
    try:
        print(Fore.LIGHTMAGENTA_EX + "----------------------------------------------------")         
        new_username = input("Enter the new username: ")
        user.update_username(new_username)
        print(Fore.LIGHTGREEN_EX + f"Success: Username updated to {new_username}")
    except Exception as exc:
        print(Fore.RED + "Error changing username: ", exc)

def all_todos(user):
    try:
        # Get all todos for the user from the database
        todos = user.get_todos()

        # Check if there are any todos for the user
        if not todos:
            print(Fore.RED + "You have no todos")
            return
        
        print(Fore.LIGHTMAGENTA_EX + "----------------------------------------------------")      
        # Print the list of todos with their IDs
        print(Fore.BLUE + "Your todos sorted by date:")
        for todo in todos:
            print(Fore.LIGHTMAGENTA_EX + "******")
            print(Fore.LIGHTWHITE_EX+ f"//-> Todo: {todo.task} //-> DueDate: {todo.due_date_date}")
    except Exception as exc:
        print(Fore.RED + "Error getting todos: ", exc)

def category_todos(user):
    try:
        # Get all categories
        categories = session.query(Category).all()
        print(Fore.LIGHTMAGENTA_EX + "----------------------------------------------------") 
        # loop through categories
        for category in categories:
            print(Fore.LIGHTYELLOW_EX + f">>> {category.name}")
            todos = category.get_todos()

            # Filter todos by user
            user_todos = [todo for todo in todos if todo.user_name == user.username]

            # Print todos for the current category and user
            for i, todo in enumerate(user_todos):
                print(Fore.LIGHTWHITE_EX+ f"{i+1}. {todo.task} (Due Date: {todo.due_date_date})")
                

    except Exception as exc:
        print(Fore.RED + "Error getting todos:", exc)
