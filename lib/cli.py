from helpers import (
    exit_program,
    add_todo
)

def main():
    while True:
        menu()
        choice = input("-> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            add_todo()
            return_or_continue()


def menu():
    print("Welcome to your trusted todo manager!")
    print("Select what you would like to do: ")
    print("0. Exit the manager")
    print("1. Add a todo")

def return_or_continue():
    print("Would you like to return to the menu or exit?")
    print("1. Return to the menu")
    print("2. Exit")
    choice = input("> ")
    if choice == "1":
        return
    elif choice == "2":
        exit()

if __name__ == "__main__":
    main()