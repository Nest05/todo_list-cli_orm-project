from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, UniqueConstraint, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id_ = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    todos = relationship('ToDo')

class Category(Base):
    __tablename__ = 'categories'

    id_ = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    todos = relationship('ToDo')

class DueDate(Base):
    __tablename__ = 'due_dates'

    id_ = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)

    todos =relationship('ToDo')


class ToDo(Base):
    __tablename__ = 'todos'

    id_ = Column(Integer, primary_key=True)
    task = Column(String, nullable=False)

    user_id = Column(Integer, ForeignKey('users.id_'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id_'), nullable=False)
    due_date_id = Column(Integer, ForeignKey('due_dates.id_'), nullable=False)

    user = relationship("User", back_populates='todos')
    category = relationship("Category", back_populates='todos')
    due_date = relationship("DueDate", back_populates='todos')




engine = create_engine('sqlite:///todo.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()