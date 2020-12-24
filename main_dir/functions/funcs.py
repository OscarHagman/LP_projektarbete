import datetime
from main_dir.pickle_db import data_handler as db

#  CONSTANTS
LIST = db.LIST  # This is the key for the dict
ID = db.ID      # This is the key for the dict


def create_reminder():
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
