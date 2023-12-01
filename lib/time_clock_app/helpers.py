import os
import getpass
import datetime
import csv
from sqlalchemy import func
from models import User
from timelog import TimeLog

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def green_text(text):
    return f"\033[92m{text}\033[0m"

def red_text(text):
    return f"\033[91m{text}\033[0m"

def display_clock():
    now = datetime.datetime.now()
    print(f"Time: {now.strftime('%I:%M:%S %p')}")

def register_user(session):
    os.system('cls' if os.name == 'nt' else 'clear')
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ") 
    new_user = User.create(username, password, session)
    if new_user:
        print(f"User {username} created successfully. User ID is: {new_user.id}")
    else:
        print("Error creating user.")

def user_info(session):
    user_id = input("Enter your user ID: ")
    user = session.query(User).get(user_id)
    if user:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Username: {user.username}")
        total_hours = user.total_hours_worked()
        print(f"Total hours worked: {total_hours:.2f} hours")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("User not found.")


def exit_program():
    print("Goodbye!")
    os.system('cls' if os.name == 'nt' else 'clear')
    exit()

def clock_in_user(session):
    user_id = int(input("Enter your user ID: "))
    user = session.query(User).get(user_id)
    if user:
        # Check if the user has already clocked in without clocking out
        latest_time_log = (session.query(TimeLog)
                           .filter_by(user_id=user.id, clock_out_time=None)
                           .order_by(TimeLog.clock_in_time.desc())
                           .first())
        if latest_time_log:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("You are already clocked in.")
        else:
            TimeLog.clock_in(user, session)
    else:
        print("User not found.")


def clock_out_user(session):
    user_id = int(input("Enter your user ID: "))
    user = session.query(User).get(user_id)
    if user:
        # Check if the user has an ongoing time log
        latest_time_log = (session.query(TimeLog)
                           .filter_by(user_id=user.id, clock_out_time=None)
                           .first())
        if latest_time_log:
            TimeLog.clock_out(user, session)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("You are not currently clocked in or you have already clocked out.")
    else:
        print("User not found.")

def admin_login():
    username = input("Enter admin username: ")
    password = getpass.getpass("Enter admin password: ")
    if username == "admin" and password == "admin":  
        os.system('cls' if os.name == 'nt' else 'clear')
        return True
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Admin login failed. Please try again.")
        return False

def list_all_users(session):
    users = session.query(User).all()
    for user in users:
        print(f"ID: {user.id}, Username: {user.username}")

def delete_user(session):
    user_id = input("Enter the ID of the user to delete: ")
    user = session.query(User).get(user_id)
    if user:
        confirm = input(f"Are you sure you want to delete {user.username}? (yes/no): ")
        if confirm.lower() == 'yes':
            session.delete(user)
            session.commit()
            os.system('cls' if os.name == 'nt' else 'clear')
            print("User deleted successfully.")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("User deletion canceled.")
    else:
        print("User not found.")

def reset_user_password(session):
    user_id = input("Enter the ID of the user to reset password: ")
    user = session.query(User).get(user_id)
    if user:
        new_password = getpass.getpass("Enter the new password: ")
        user.password = new_password  
        session.commit()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Password for {user.username} reset successfully.")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("User not found.")

def edit_time_log(session, user_id, new_clock_in=None, new_clock_out=None):
    time_log = session.query(TimeLog).filter(TimeLog.user_id == user_id).first()
    if not time_log:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Time log not found.")
        return

    if new_clock_in:
        time_log.clock_in_time = new_clock_in
    if new_clock_out:
        time_log.clock_out_time = new_clock_out

    session.commit()
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Time log updated for user {user_id}.")

def view_all_time_logs(session, filter_by_user=None, filter_by_date=None):
    query = session.query(TimeLog)
    if filter_by_user:
        query = query.filter(TimeLog.user_id == filter_by_user)
    if filter_by_date:
        query = query.filter(TimeLog.clock_in_time >= filter_by_date)

    for log in query.all():
        print(f"User ID: {log.user_id}, Clock In: {log.clock_in_time}, Clock Out: {log.clock_out_time}")

import datetime

def generate_report(session, user_id=None, start_date=None, end_date=None):
    
    query = session.query(
        TimeLog.user_id,
        TimeLog.clock_in_time,
        TimeLog.clock_out_time
    )

 
    if user_id:
        query = query.filter(TimeLog.user_id == user_id)
    if start_date:
        query = query.filter(TimeLog.clock_in_time >= start_date)
    if end_date:
        query = query.filter(TimeLog.clock_in_time <= end_date)

    
    raw_data = query.all()

    
    total_hours = {}
    for record in raw_data:
        user, clock_in, clock_out = record.user_id, record.clock_in_time, record.clock_out_time
        if clock_out and clock_in: 
            duration = (clock_out - clock_in).total_seconds() / 3600
            if user in total_hours:
                total_hours[user] += duration
            else:
                total_hours[user] = duration

    
    report_data = [(user, hours) for user, hours in total_hours.items()]
    return report_data

def export_report_to_csv(report_data, filename):
    with open(f'{filename}.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['User ID', 'Total Hours Worked'])

        for user_id, total_hours in report_data:
            writer.writerow([user_id, total_hours])