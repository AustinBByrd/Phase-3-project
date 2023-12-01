# Time Tracking CLI Application

## Introduction
This repository contains a Python-based CLI (Command Line Interface) application designed for time tracking. This tool is particularly useful for managing employee clock-in and clock-out times, viewing and editing time logs, and generating reports.

## Features
- **User Management**: Register new users, view user information, and delete users.
- **Time Tracking**: Users can clock in and clock out. Administrators can view and edit time logs for all users.
- **Reports**: Generate and export time tracking reports.
- **Admin Panel**: Special administrative functionalities for managing users and viewing detailed logs.
- **User-Friendly Interface**: Easy-to-navigate menu options with clear, centered text display.

## Installation
To install this application, follow these steps:

1. Clone the repository:
  git clone https://github.com/AustinBByrd/Phase-3-project

3. Navigate to the cloned directory:
   cd [cloned-directory-name]
   
3. Install required dependencies:
   
   pipenv install

   pipenv shell
   
## Usage
To use this application:

1. Run the script from inside lib/time_clock_app:

   python cli.py
   
3. Follow the on-screen prompts to navigate through the menu options.

## Generate Data script
To use this application:

1. Run the script from inside lib/time_clock_app:

  python gen_data.py

#### This will generate a random timeclock.db if one does not exist or modify the current one with Users and Timelogs
   

## Contributing
Contributions to this project are welcome. To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.
