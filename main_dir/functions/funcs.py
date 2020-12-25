import datetime
from main_dir.pickle_db import data_handler as db

#  CONSTANTS
LIST = db.LIST  # This is the key for the dict
ID = db.ID      # This is the key for the dict

PATH_PYTHON_TEMPLATE = db.PATH_PYTHON_TEMPLATE
SAVE_PYTHON_PATH = db.PATH_EMAIL_SCRIPTS  # Path for where to save the python email script


def create_email_scripts(id_number, receiver_email) -> None:
    """
    Writes a custom and unique .py, .service and .timer file based on templates.
    The .py file opens the .pickle file, searches for a matching id number and attaches the title and text to the
    message that will be sent to the receiver_email address.

    The .service file will execute the .py file.

    The .timer file will execute the .service file at the given date & time

    :param id_number: Is used to locate correct data to send in the email and to create unique file names.
    :param receiver_email: Email address the .py file will send that data to.
    :param timestamp: Will set what date & time the .timer file will execute the .service file.
    """
    receiver_email = '"' + receiver_email + '"'  # Ads "" to the string so it gets represented as a string in the script
    create_file_path = SAVE_PYTHON_PATH + "reminder_" + str(id_number) + ".py"  # Creates a unique file name
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


def create_service(id_number):
    pass


def create_timer(id_number):
    pass


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
