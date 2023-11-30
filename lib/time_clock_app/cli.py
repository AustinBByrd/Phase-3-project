import os
import time
from datetime import datetime
from colorama import init, Fore, Back, Style
from reports import generate_report_option, export_report_option
from database import Session, initialize_db
from helpers import (
    exit_program,
    register_user,
    user_info,
    clock_in_user,
    clock_out_user,
    admin_login,
    list_all_users,
    delete_user,
    reset_user_password,
    edit_time_log, 
    view_all_time_logs
)

os.system('cls' if os.name == 'nt' else 'clear')
init(autoreset=True)

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
            os.system('cls' if os.name == 'nt' else 'clear')
            if admin_login():  
                admin_menu(session)
        elif choice == "0":
            exit_program()
        else:
            print("Invalid choice")

def get_current_time():
    current_time = time.localtime()
    formatted_time = time.strftime("%I:%M %p", current_time) 
    return formatted_time

def create_button(label, width):
    color_text = Fore.MAGENTA
    color_bg = Back.YELLOW
    reset = Style.RESET_ALL
    # Create a single button with top, middle, and bottom parts.
    top_bottom = color_bg + '+' + '-' * (width - 2) + '+' + reset
    middle = color_bg + '|' + color_text + label.center(width - 2) + '|' + reset
    return top_bottom, middle, top_bottom

def print_grid_menu(options, width):
    # Print menu options in a grid layout.
    for i in range(0, len(options), 2):
        left_top, left_middle, left_bottom = create_button(options[i], width)
        if i + 1 < len(options):
            right_top, right_middle, right_bottom = create_button(options[i + 1], width)
        else:
            right_top, right_middle, right_bottom = ' ' * width, ' ' * width, ' ' * width
        print(left_top + ' ' + right_top)
        print(left_middle + ' ' + right_middle)
        print(left_bottom + ' ' + right_bottom)
        print()

button_width = 40
def menu():
    # os.system('cls' if os.name == 'nt' else 'clear')
    current_time = get_current_time() 
    print(f"Current Time: {current_time}")
    print("Please select an option:")
    # Define menu options for the grid layout.
    menu_options = [
        "1. Clock in", "2. Clock out",
        "3. View user information", "4. Admin login",
        "0. Exit the program"
    ]
    # Assuming a console width that can accommodate 40 characters per button.
    print_grid_menu(menu_options, button_width)

def admin_menu(session):
    while True:

        current_time = get_current_time()
        print(f"Current Time: {current_time}")
        print("Admin Menu:")
        
        # Define admin menu options for the grid layout.
        admin_options = [
            "1. Register new user", "2. List all users",
            "3. Delete a user", "4. Reset user password",
            "5. Time Logs", "6. Reports",
            "7. Return to main menu", "0. Exit the program"
        ]
        
        # Print admin menu in grid layout.
        print_grid_menu(admin_options, button_width)
        
        admin_choice = input("> ")
        if admin_choice == "1":
            register_user(session)
        elif admin_choice == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            list_all_users(session)
        elif admin_choice == "3":
            delete_user(session)
        elif admin_choice == "4":
            reset_user_password(session)
        elif admin_choice == "5":
            os.system('cls' if os.name == 'nt' else 'clear')
            time_logs_menu(session)
        elif admin_choice == "6":
            os.system('cls' if os.name == 'nt' else 'clear')
            reports_menu(session)
        elif admin_choice == "7":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        elif admin_choice == "0":
            exit_program()


def time_logs_menu(session):
    while True:
        print("\nTime Logs Menu")
        print("1. Edit Time Log")
        print("2. View All Time Logs")
        print("0. Back to Admin Menu")
        choice = input("> ")

        if choice == "1":
            edit_time_log_option(session)
        elif choice == "2":
            view_all_time_logs_option(session)
        elif choice == "0":
            break
        else:
            print("Invalid choice")

def reports_menu(session):
    while True:
        print("\nReports Menu")
        print("1. Generate Report")
        print("2. Export Report to CSV")
        print("0. Back to Admin Menu")
        choice = input("> ")

        if choice == "1":
            report_data = generate_report_option(session)
        elif choice == "2" and 'report_data' in locals():
            export_report_option(report_data)
        elif choice == "0":
            break
        else:
            print("Invalid choice")

def edit_time_log_option(session):
    user_id = input("Enter User ID to edit time log: ")
    new_clock_in = input("Enter new Clock In time (YYYY-MM-DD HH:MM:SS), leave blank if no change: ")
    new_clock_out = input("Enter new Clock Out time (YYYY-MM-DD HH:MM:SS), leave blank if no change: ")
    edit_time_log(session, user_id, new_clock_in, new_clock_out)

def view_all_time_logs_option(session):
    filter_user = input("Enter User ID to filter by, leave blank for no filter: ")
    filter_date = input("Enter date to filter by (YYYY-MM-DD), leave blank for no filter: ")
    view_all_time_logs(session, filter_user, filter_date)

if __name__ == "__main__":
    initialize_db()
    main()
