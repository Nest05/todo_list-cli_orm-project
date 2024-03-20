from db.models import User, ToDo, Category, DueDate, session
from datetime import datetime

def add_todo():
    user = session.query(User).filter_by(username="William Steele").first()
    task = input("Enter the task: ")
    category_name = input("Enter the category: ")
    due_date_str = input("Enter the due date (YYYY-MM-DD HH:MM:SS): ")


    try:
        # Retrieve category and due date objects based on input values
        category = session.query(Category).filter_by(name=category_name).first()
        due_date = DueDate(date=datetime.strptime(due_date_str, "%Y-%m-%d %H:%M:%S"))

        todo = user.create_todo(task, category, due_date)
        print(f'Success: <{task}> added to your todos!')
    except Exception as exc:
        print("Error creating todo: ", exc)

add_todo()
