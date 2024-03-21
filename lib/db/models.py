from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, UniqueConstraint, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id_ = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    todos = relationship('ToDo')

    def create_todo(self, task, category, due_date):
        # Create a new todo item for this user
        todo = ToDo(task=task, category=category, due_date=due_date, user=self)
        session.add(todo)
        session.commit()
        return todo
    
    def delete_todo(self, todo_id):
        # Delete a todo item for this user by its Id
        todo =session.query(ToDo).filter_by(id_=todo_id, user=self).first()
        if todo:
            session.delete(todo)
            session.commit()
    
    def update_username(self, new_username):
        # Update the username for this user
        self.username = new_username
        session.commit()

    def get_todos(self):
        # Get all todos for this user
        todos = session.query(ToDo).filter_by(user=self).order_by(ToDo.due_date_date).all()
        return todos
    

class Category(Base):
    __tablename__ = 'categories'

    id_ = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    todos = relationship('ToDo')

    def get_todos(self):
        # Get all todo items in this category
        todos = session.query(ToDo).filter_by(category=self).all()
        return todos

class DueDate(Base):
    __tablename__ = 'due_dates'

    id_ = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)

    todos =relationship('ToDo')
    
    def get_todos(self):
        # Get all todos with due date
        todos = session.query(ToDo).filter_by(due_date=self).all()
        return todos


class ToDo(Base):
    __tablename__ = 'todos'

    id_ = Column(Integer, primary_key=True)
    task = Column(String, nullable=False)

    user_name = Column(Integer, ForeignKey('users.username'), nullable=False)
    category_name = Column(Integer, ForeignKey('categories.name'), nullable=False)
    due_date_date = Column(Integer, ForeignKey('due_dates.date'), nullable=False)

    user = relationship("User", back_populates='todos')
    category = relationship("Category", back_populates='todos')
    due_date = relationship("DueDate", back_populates='todos')

    def update_task(self, new_task):
        # update the task for this todo
        self.task = new_task
        session.commit()
    
    def update_category(self, new_category):
        # update the category for this todo 
        self.category = new_category
        session.commit()

    def update_due_date(self, new_due_date):
        # update the due date for this todo
        self.due_date = new_due_date
        session.commit()



engine = create_engine('sqlite:///todo.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()