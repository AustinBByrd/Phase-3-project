from database import Session, initialize_db
from helpers import (
    exit_program,
    register_user,
    user_info,
    clock_in_user,
    clock_out_user,
    admin_login
)

def main():
    session = Session()
    while True:
        menu()
        choice = input("> ")
        if choice == "1":
            clock_in_user(session)
        elif choice == "2":
            clock_out_user(session)
        elif choice == "3":
            user_info(session)
        elif choice == "4":
            if admin_login():  
                admin_menu(session)
        elif choice == "0":
            exit_program()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("1. Clock in")
    print("2. Clock out")
    print("3. View user information")
    print("4. Admin login")
    print("0. Exit the program")

def admin_menu(session):
    while True:
        print("Admin Menu:")
        print("1. Register new user")
        print("2. Return to main menu")
        admin_choice = input("> ")
        if admin_choice == "1":
            register_user(session)
        elif admin_choice == "2":
            break

if __name__ == "__main__":
    initialize_db()
    main()
