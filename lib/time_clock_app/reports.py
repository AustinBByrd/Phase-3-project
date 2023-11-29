from database import Session
from helpers import generate_report, export_report_to_csv
import os
from datetime import datetime

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