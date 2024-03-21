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

# def remove_todo():

