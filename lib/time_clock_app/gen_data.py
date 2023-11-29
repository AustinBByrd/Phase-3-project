from faker import Faker
import random
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base
from models import User
from timelog import TimeLog

# Initialize Faker
fake = Faker()

# Database setup
engine = create_engine('sqlite:///timeclock.db')
Session = sessionmaker(bind=engine)
session = Session()

# Function to initialize the database
def initialize_db():
    Base.metadata.create_all(engine)

# Function to generate random work hours for each day of the week
def generate_work_hours(total_hours):
    days = [0] * 5  # Assuming a 5-day work week
    while total_hours > 0:
        index = random.randint(0, 4)  # Select a random day
        hours = random.randint(1, min(8, total_hours))  # Random hours, max 8 per day
        days[index] += hours
        total_hours -= hours
    return days

# Function to create time logs for each day with work hours
def create_time_logs(start_date, work_hours, user):
    logs = []
    for i, hours in enumerate(work_hours):
        if hours > 0:
            clock_in = start_date + datetime.timedelta(days=i, hours=8)  # Assuming work starts at 8 AM
            clock_out = clock_in + datetime.timedelta(hours=hours)

            # Create a TimeLog instance and set attributes after creation
            time_log = TimeLog(user=user)
            time_log.clock_in_time = clock_in
            time_log.clock_out_time = clock_out

            logs.append(time_log)
    return logs

# Function to create users and their time logs
def create_users_and_logs(num_users):
    for _ in range(num_users):
        # Generate a proper first and last name
        first_name = fake.first_name()
        last_name = fake.last_name()
        full_name = f"{first_name} {last_name}"

        password = fake.password()
        user = User(username=full_name, password=password)
        session.add(user)
        session.commit()

        # Generate work hours and time logs for the user
        total_hours = random.randint(10, 45)  # Total hours for a week
        start_date = datetime.datetime.now() - datetime.timedelta(weeks=1)
        work_hours = generate_work_hours(total_hours)
        time_logs = create_time_logs(start_date, work_hours, user)

        for log in time_logs:
            session.add(log)
        session.commit()


# Initialize the database and create users with time logs
if __name__ == '__main__':
    initialize_db()
    create_users_and_logs(20)
