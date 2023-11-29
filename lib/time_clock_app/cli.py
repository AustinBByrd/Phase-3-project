import os
import subprocess
import time
from datetime import datetime

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
    view_all_time_logs,
    generate_report,
    export_report_to_csv
)

os.system('cls' if os.name == 'nt' else 'clear')

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

def menu():
    current_time = get_current_time() 
    print(f"Current Time: {current_time}")
    print("Please select an option:")
    print("1. Clock in")
    print("2. Clock out")
    print("3. View user information")
    print("4. Admin login")
    print("0. Exit the program")

def admin_menu(session):
    while True:
        current_time = get_current_time()
        print(f"Current Time: {current_time}")
        print("Admin Menu:")
        print("1. Register new user")
        print("2. List all users")
        print("3. Delete a user")
        print("4. Reset user password")
        print("5. Time Logs")
        print("6. Reports")
        print("7. Return to main menu")
        print("0. Exit the program")
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

def generate_report_option(session):
    user_id_input = input("Enter User ID for specific user report, leave blank for all users: ")
    user_id = int(user_id_input) if user_id_input else None

    start_date_str = input("Enter start date (YYYY-MM-DD), leave blank for no start date: ")
    end_date_str = input("Enter end date (YYYY-MM-DD), leave blank for no end date: ")

    start_date = None
    end_date = None

    try:
        if start_date_str:
            start_date = datetime.fromisoformat(start_date_str)
        if end_date_str:
            end_date = datetime.fromisoformat(end_date_str)
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return


    report_data = generate_report(session, user_id, start_date, end_date)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Report generated successfully.")
    return report_data


def export_report_option(report_data):
    filename = input("Enter filename for the CSV export: ")
    export_report_to_csv(report_data, filename)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Report exported to {filename}.csv")

if __name__ == "__main__":
    initialize_db()
    main()
