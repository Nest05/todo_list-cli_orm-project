from helpers import (
    exit_program,
    login,
    add_todo,
    remove_todo
)

def main():
    user = None # Initialize user as None
    while True:
        if user is None: # Check if user is not logged in
            login_menu()
            choice = input("-> ")
            if choice == "0":
                exit_program()
            elif choice == "1":
                user = login()
                try_again()
        else:
            sub_main(user)

def sub_main(user):
    while True:
        menu()
        choice = input("-> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            add_todo(user)
            return_or_exit()
        elif choice == "2":
            remove_todo(user)
            return_or_exit()

def menu():
    print("----------------------------------------------------")
    print("***Todo Menu***")
    print("Select what you would like to do: ")
    print("0. Exit the manager")
    print("1. Add a todo")
    print("2. Remove a todo")

def login_menu():
    print("----------------------------------------------------")
    print("Welcome to your trusted todo manager!")
    print("login below: ")
    print("0. Exit the manager")
    print("1. Login")

def return_or_exit():
    print("----------------------------------------------------")
    print("Would you like to return to the menu or exit?")
    print("1. Return to the menu")
    print("2. Exit")
    choice = input("> ")
    if choice == "1":
        return
    elif choice == "2":
        exit_program()

def try_again():
    print("----------------------------------------------------")
    print("Would you like to try again or exit?")
    print("1. Return to the login menu")
    print("2. Exit")
    choice = input("> ")
    if choice == "1":
        return
    elif choice == "2":
        exit_program()

if __name__ == "__main__":
    main()