from faker import Faker
from models import User, ToDo, Category, DueDate, session

f = Faker()

# Create a user
user = User(username=f.name(), password=f.password())
session.add(user)

# Create categories
categories = ['Work', 'Personal', 'Study','Travel']
category_objects = []
for category_name in categories:
    category = Category(name=category_name)
    session.add(category)
    category_objects.append(category)

# Create due dates
due_dates = [f.future_datetime() for _ in range(4)]
due_date_objects = []
for due_date in due_dates:
    due_date_obj = DueDate(date=due_date)
    session.add(due_date_obj)
    due_date_objects.append(due_date_obj)

# Create todos
for _ in range(5):
    task = f.sentence()
    category = f.random_element(category_objects)
    due_date = f.random_element(due_date_objects)

    todo = ToDo(task=task, user=user, category=category, due_date=due_date)
    session.add(todo)

# Commit the changes to the database
session.commit()