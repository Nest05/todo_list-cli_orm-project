from helpers import (
    exit_program,
    login,
    add_todo
)

def main():
    while True:
        login_menu()
        choice = input("-> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            add_todo()
            return_or_exit()

def menu():
    print("----------------------------------------------------")
    print("You have successfully logged in!")
    print("Select what you would like to do: ")
    print("0. Exit the manager")
    print("1. Add a todo")

def login_menu():
    print("----------------------------------------------------")
    print("Welcome to your trusted todo manager!")
    print("login below: ")
    print("0. Exit the manager")
    print("1. Login")

def return_or_exit():
    print("----------------------------------------------------")
    print("Would you like to return to the login menu or exit?")
    print("1. Return to the login menu")
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