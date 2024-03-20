from faker import Faker
from models import User, ToDo, Category, DueDate, session

# Assign faker to a variable
f = Faker()

# Create empty lists to store user, category and due date objects
users = []
categories = []
due_date_objects = []

# Create users
for _ in range(5):
    user = User(username=f.name(), password=f.password())
    session.add(user)
    users.append(user)

# Create categories
category_names = ['Work', 'Personal', 'Study','Travel']
categories = []
for category_name in category_names:
    category = Category(name=category_name)
    session.add(category)
    categories.append(category)

# Create due dates
due_dates = [f.future_datetime() for _ in range(20)]
for due_date in due_dates:
    due_date_obj = DueDate(date=due_date)
    session.add(due_date_obj)
    due_date_objects.append(due_date_obj)

# Create todos
for _ in range(20):
    task = f.sentence()
    category = f.random_element(categories)
    due_date = f.random_element(due_date_objects)

    user = users[_ % len(users)]

    todo = ToDo(task=task, user=user, category=category, due_date=due_date)
    session.add(todo)

# Commit the changes to the database
session.commit()