from art import *
from colorama import init, Fore
init(autoreset=True)

from helpers import (
    exit_program,
    login,
    add_todo,
    remove_todo,
    change_username,
    all_todos,
    category_todos,
    add_user,
    change_task,
    change_category
)
tprint("BespokeRoutine", font="random")
def main():
    user = None # Initialize user as None
    options = ["0", "1", "2"] # Valid options
    while True:
        if user is None: # Check if user is not logged in
            login_menu()
            choice = input("-> ")
            if choice not in options: # Check if choice is not in the valid options
                print(Fore.RED + "Invalid input. Please try again.")
                continue # Go back to the beginning of the loop
            if choice == "0":
                exit_program()
            elif choice == "1":
                user = login()
                try_again()
            elif choice == "2":
                add_user()
                try_again()
        else:
            sub_main(user)

def sub_main(user):
    options = ["0", "1", "2", "3", "4", "5", "6", "7"] # Valid options
    while True:
        menu()
        choice = input("-> ")
        if choice not in options: # Check if choice is not in the valid options
            print(Fore.RED + "Invalid input. Please try again.")
            continue
        if choice == "0":
            exit_program()
        elif choice == "1":
            add_todo(user)
            return_or_exit()
        elif choice == "2":
            remove_todo(user)
            return_or_exit()
        elif choice == "3":
            change_username(user)
            return_or_exit()
        elif choice == "4":
            all_todos(user)
            return_or_exit()
        elif choice == "5":
            category_todos(user)
            return_or_exit()
        elif choice == "6":
            change_task(user)
            return_or_exit()
        elif choice == "7":
            change_category(user)
            return_or_exit()

def menu():
    print(Fore.LIGHTMAGENTA_EX + "----------------------------------------------------")
    tprint(" ***Todo Menu*** ", font="small")
    print(Fore.LIGHTCYAN_EX + "Select what you would like to do: ")
    print(Fore.RED + "0. Exit the manager")
    print("1. Add a todo")
    print("2. Remove a todo")
    print("3. Change username")
    print("4. See all my todos")
    print("5. Todos by category")
    print("6. Edit a task")
    print("7. Change a task's category")

def login_menu():
    print(Fore.LIGHTMAGENTA_EX + "----------------------------------------------------")
    print(Fore.LIGHTCYAN_EX + "\U0001F5D2  Welcome to your trusted todo manager! \U0001F4D3")
    print("login below: ")
    print(Fore.RED + "0. Exit the manager")
    print("1. Login")
    print("2. Signup")

def return_or_exit():
    options = ["1", "2"] # Valid options
    print(Fore.LIGHTMAGENTA_EX + "----------------------------------------------------")
    print(Fore.LIGHTCYAN_EX + "Would you like to return to the menu or exit?")
    print("1. Return to the menu")
    print(Fore.RED + "2. Exit")
    choice = input("> ")
    if choice not in options: # Check if choice is not in the valid options
        print(Fore.RED + "Invalid input. Please try again.")
        return
    if choice == "1":
        return
    elif choice == "2":
        exit_program()

def try_again():
    options = ["1", "2"] # Valid options
    print(Fore.LIGHTMAGENTA_EX + "----------------------------------------------------")
    print(Fore.LIGHTCYAN_EX + "Would you like to the login menu or exit?")
    print("1. Return to the login menu")
    print(Fore.RED + "2. Exit")
    choice = input("> ")
    if choice not in options: # Check if choice is not in the valid options
        print(Fore.RED + "Invalid input. Please try again.")
        return
    if choice == "1":
        return
    elif choice == "2":
        exit_program()

if __name__ == "__main__":
    main()