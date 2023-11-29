import os
from models import User
from timelog import TimeLog


def register_user(session):
    os.system('cls' if os.name == 'nt' else 'clear')
    username = input("Enter username: ")
    password = input("Enter password: ") 
    new_user = User.create(username, password, session)
    if new_user:
        print(f"User {username} created successfully. User ID is: {new_user.id}")
    else:
        print("Error creating user.")

def user_info(session):
    os.system('cls' if os.name == 'nt' else 'clear')
    user_id = input("Enter your user ID: ")
    user = session.query(User).get(user_id)
    if user:
        print(f"Username: {user.username}")
        total_hours = user.total_hours_worked()
        print(f"Total hours worked: {total_hours:.2f} hours")
    else:
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
        print("User not found.")

def clock_out_user(session):
    user_id = int(input("Enter your user ID: "))
    user = session.query(User).get(user_id)
    if user:
        TimeLog.clock_out(user, session)
        print("Clocked out successfully.")
    else:
        print("User not found.")

def admin_login():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    return username == "admin" and password == "admin"
