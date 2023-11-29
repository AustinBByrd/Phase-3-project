import os
import getpass
from models import User
from timelog import TimeLog


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
        TimeLog.clock_in(user, session)
        print("Clocked in successfully.")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("User not found.")

def clock_out_user(session):
    user_id = int(input("Enter your user ID: "))
    user = session.query(User).get(user_id)
    if user:
        TimeLog.clock_out(user, session)
        print("Clocked out successfully.")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("User not found.")

def admin_login():
    username = input("Enter admin username: ")
    password = getpass.getpass("Enter admin password: ")
    if username == "admin" and password == "admin":  
        os.system('cls' if os.name == 'nt' else 'clear')
        return True
    else:
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
        print("Time log not found.")
        return

    if new_clock_in:
        time_log.clock_in_time = new_clock_in
    if new_clock_out:
        time_log.clock_out_time = new_clock_out

    session.commit()
    print(f"Time log updated for user {user_id}.")

def view_all_time_logs(session, filter_by_user=None, filter_by_date=None):
    query = session.query(TimeLog)
    if filter_by_user:
        query = query.filter(TimeLog.user_id == filter_by_user)
    if filter_by_date:
        query = query.filter(TimeLog.clock_in_time >= filter_by_date)

    for log in query.all():
        print(f"User ID: {log.user_id}, Clock In: {log.clock_in_time}, Clock Out: {log.clock_out_time}")