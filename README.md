# Simple ToDO List Maneger

This is a CLI(Command Line Interface)+ORM(Object-Relational Mapper) project, using Python

## Description

This todo manager enable you to create tables and store data about your todos.
- It requires a simple sign up for access
- After, signing up you can then log in and start the process of:
-> Adding todos
-> See all todos added
-> Remove/Delete a todo
-> Change user name
-> See your todos by categrory
- Todos are sorted by date, so the one with the earliest deadline is always first on the list

## Requirements
You need to implement a Python CLI Application that meets the following requirements.

### ORM Requirements
- The application must include a database created and modified with Python ORM methods that you write.

- The data model must include at least 2 model classes.
- The data model must include at least 1 one-to-many relationships.
- Property methods should be defined to add appropriate constraints to each model class.
- Each model class should include ORM methods (create, delete, get all, and find by id at minimum).

### CLI Requirements
- The CLI must display menus with which a user may interact.
- The CLI should use loops as needed to keep the user in the application until they choose to exit.
- For EACH class in the data model, the CLI must include options: to create an object, delete an object, display all objects, view related objects, and find an object by attribute.
- The CLI should validate user input and object creations/deletions, providing informative errors to the user.
- The project code should follow OOP best practices.
- Pipfile contains all needed dependencies and no unneeded dependencies.
- Imports are used in files only where necessary.
- Project folders, files, and modules should be organized and follow appropriate naming conventions.
- The project should include a README.md that describes the application.
- You do not need to implement tests for pytest, although you should test your code thoroughly using your CLI. Try entering bad data when prompted for input, and confirm your application prints a useful error message.

## Technology Stack:
Back-end: Python
Database: SQLite
Frameworks/Libraries: SQLAlchemy (ORM)

## Author

- **Nestor Masinde** <[Nest05](https://github.com/Nest05)>

## Conclusion

The proposed ToDo list manager will provide users with an intuitive and efficient tool to manage their tasks, prioritize work, and improve personal productivity. By developing this application, we aim to deliver a valuable solution that helps individuals stay organized and accomplish their goals effectively.

## Resources

- [Python Tutorials and Examples](https://www.askpython.com/)
- [Python Database Tutorial](https://www.geeksforgeeks.org/python-database-tutorial/?ref=shm)

## License

[MIT License](LICENSE)
