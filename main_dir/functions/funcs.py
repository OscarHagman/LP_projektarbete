import os
import datetime
from main_dir.pickle_db import data_handler as db

#  CONSTANTS
LIST = db.LIST  # This is the key for the dict
ID = db.ID      # This is the key for the dict

PATH_PYTHON_TEMPLATE = db.PATH_PYTHON_TEMPLATE
PATH_PROJECT = db.PATH_PROJECT  # Path for where the python email scripts are saved

PATH_SERVICE_TEMPLATE = db.PATH_SERVICE_TEMPLATE
PATH_TIMER_TEMPLATE = db.PATH_TIMER_TEMPLATE
SYSTEMD_PATH = "/etc/systemd/system/"


def execute_timer(daemon_name):
    d_timer = daemon_name + ".timer"
    d_python = "/" + daemon_name + ".py"

    os.system("sudo chmod +x " + PATH_PROJECT + d_python)
    os.system("sudo systemctl daemon-reload")
    os.system("sudo systemctl enable " + d_timer)
    os.system("sudo systemctl start " + d_timer)


def create_service(email_script_path, daemon_name):
    with open(PATH_SERVICE_TEMPLATE, "r") as template:
        template_list = template.readlines()
    #  Removes the '\n' from the end of each element and ads the item into a new list
    edited_list = []
    for item in template_list:
        edited_item = item.strip("\n")
        edited_list.append(edited_item)

    #  Finds where ExecStart is and ads to the element what path to take for the email script
    exec_start_index = edited_list.index("ExecStart=")
    edited_exec_start = (edited_list[exec_start_index] + email_script_path)
    #  Ads the edited ExecStart item to the edited list, which will be printed to a new file
    edited_list[exec_start_index] = edited_exec_start

    create_file_path = SYSTEMD_PATH + "/" + daemon_name + ".service"
    # Creates a new .service file in the given path and writes the custom service to the file
    with open(create_file_path, "w") as email_service:
        for line in edited_list:
            print(line, file=email_service)


def create_timer(time_stamp, daemon_name):
    with open(PATH_TIMER_TEMPLATE, "r") as template:
        template_list = template.readlines()
    #  Removes the '\n' from the end of each element and ads the item into a new list
    edited_list = []
    for item in template_list:
        edited_item = item.strip("\n")
        edited_list.append(edited_item)

    #  Finds where OnCalendar is and ads to the element what date & time to execute
    on_calendar_index = edited_list.index("OnCalendar=")
    edited_on_calendar = (edited_list[on_calendar_index] + time_stamp + ":00")
    #  Ads the edited OnCalendar item to the edited list, which will be printed to a new file
    edited_list[on_calendar_index] = edited_on_calendar

    create_file_path = SYSTEMD_PATH + "/" + daemon_name + ".timer"
    # Creates a new .service file in the given path and writes the custom service to the file
    with open(create_file_path, "w") as email_service:
        for line in edited_list:
            print(line, file=email_service)


def create_email_script(id_number, receiver_email, daemon_name, handler) -> None:
    """
    Writes a custom and unique .py, .service and .timer file based on templates.
    The .py file opens the .pickle file, searches for a matching id number and attaches the title and text to the
    message that will be sent to the receiver_email address.

    The .service file will execute the .py file.

    The .timer file will execute the .service file at the given date & time

    :param id_number: Is used to locate correct data to send in the email and to create unique file names.
    :param receiver_email: Email address the .py file will send that data to.
    :param daemon_name: For creating unique file name
    """
    handler.load_reminder()  # Load the files so we can find correct data with the id number

    receiver_email = '"' + receiver_email + '"'  # Ads "" to the string so it gets represented as a string in the script
    create_file_path = PATH_PROJECT + "/" + daemon_name + ".py"

    with open(PATH_PYTHON_TEMPLATE, "r") as template:
        template_list = template.readlines()
    #  Removes the '\n' from the end of each element and ads the item into a new list
    edited_list = []
    for item in template_list:
        edited_item = item.strip("\n")
        edited_list.append(edited_item)

    # Find where the id and email variable is in the list and ads the custom value to them
    id_index = edited_list.index("REMINDER_ID")
    receiver_index = edited_list.index("receiver_email")
    edited_reminder_id = (edited_list[id_index] + " = " + str(id_number))
    edited_receiver_email = (edited_list[receiver_index] + " = " + receiver_email)

    #  Ads the edited id number and receiver email to correct variables in the script
    edited_list[id_index] = edited_reminder_id
    edited_list[receiver_index] = edited_receiver_email

    # Creates a new .py file in the given path and writes the custom script to the file
    with open(create_file_path, "w") as email_script:
        for line in edited_list:
            print(line, file=email_script)


def yes_or_no() -> bool:
    """
    Allows the user to answer simple "yes or no" questions and lets them try again if the input is incorrect
    :return: True for "y" (yes) and False for "n" (no)
    """
    while True:
        user_choice = input("(y/n): ")
        if user_choice == "y":
            return True
        elif user_choice == "n":
            return False
        else:
            print("Invalid input, try again")


def input_to_int() -> int:
    """
    Converts user input to `int` and handles ValueError. Allows the user to try again if the input is incorrect
    :return: int
    """
    while True:
        try:
            return int(input(": "))
        except ValueError:
            print("You can only enter numbers, try again")


def multiline_input() -> str:
    """
    Allows the user to input multiple lines of Strings. The user quits by entering an empty String.
    :return: Multiline String
    """
    print("Press 'enter' with no text when you're done\n")
    lines = []
    while True:
        line = input("\t")
        if line:
            lines.append(line)
        else:
            break
    multiline_text = "\n".join(lines)
    return multiline_text


def create_reminder_timestamp() -> str:
    """
    Takes input from user for what date and time the reminder email will be sent.
    Checks if the format is correct and makes the user try again if it didn't parse
    :return: Date and time String as 'YYYY-MM-DD HH:MM'
    """
    while True:
        reminder_timestamp = input('Date & time for reminder\n"YYYY-MM-DD HH:MM": ')
        datetime_obj_to_parse = reminder_timestamp + ":00.000000"
        try:
            datetime.datetime.strptime(datetime_obj_to_parse, '%Y-%m-%d %H:%M:%S.%f')
            return reminder_timestamp
        except ValueError:
            print("You entered wrong format\nExample on correct format: 2020-04-20 13:37\n")
