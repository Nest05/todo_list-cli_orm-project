from db.models import User, ToDo, Category, DueDate, session
from faker import Faker

f = Faker()

def add_todo():
    user = session.query(User).filter_by(username="William Steele").first()
    task = input("Enter the task: ")
    category_name = input("Enter the category: ")


    # Generate a valid due date using Faker
    due_date_str = f.date_between(start_date='today', end_date='+30d')

    try:
        # Retrieve category and due date objects based on input values
        category = session.query(Category).filter_by(name=category_name).first()
        due_date = DueDate(date=due_date_str)

        todo = user.create_todo(task, category, due_date)
        print(f'Success: <{todo}> added to your todos!')
    except Exception as exc:
        print("Error creating todo: ", exc)

add_todo()
