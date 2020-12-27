from main_dir.pickle_db import data_handler as db
from main_dir.functions import funcs as f


#  CONSTANTS
LIST = db.LIST    # This is the key for the reminders list in the dict
ID = db.ID        # This is the key for the id counter in the dict
EMAIL = db.EMAIL  # This is the key for the receiver email in the dict

PATH_EMAIL_SCRIPTS = db.PATH_EMAIL_SCRIPTS


def open_reminder(reminder_index: int) -> None:
    """
    Opens the menu for the given reminder which allows the user to read, edit and delete the opened reminder.
    :param reminder_index: The index for what reminder to open
    :return: None
    """
    while True:
        opened_reminder = db.REMINDERS[LIST][reminder_index]
        print("Reminder:", opened_reminder.title, "| ID:", opened_reminder.reminder_id)
        print("[1] Read\n[2] Delete\n[3] Go back")
        to_do_menu_choice = input(": ")
        if to_do_menu_choice == "1":
            print("Date&time for reminder:", opened_reminder.reminder_date)
            print("Title:", opened_reminder.title)
            print("\n" + opened_reminder.text + "\n")

        elif to_do_menu_choice == "2":
            print("You sure you want to delete", opened_reminder.title + "?")
            if f.yes_or_no():
                del db.REMINDERS[LIST][reminder_index]  # Delete daemon process
                print(opened_reminder.title, "has been deleted")
                db.dump_reminders()
                break
        elif to_do_menu_choice == "3":
            print("Going back")
            break
        else:
            print("Invalid input")


#  PROGRAM STARTS HERE
while True:
    db.load_reminder()
    print("\n[1] Create reminder\n[2] View reminders\n[3] Set receiver email\n[4] Exit")
    main_menu_input = input(": ")

    if main_menu_input == "1":
        reminder_title = input("Reminder title: ")
        print("\nThis is a multi-line input for your reminder text")
        reminder_text = f.multiline_input()
        reminder_timestamp = f.create_reminder_timestamp()

        reminder_object = db.Reminder(reminder_title, reminder_text, reminder_timestamp, db.REMINDERS[ID])
        db.REMINDERS[LIST].append(reminder_object)
        db.dump_reminders()

        daemon_name = "reminder_" + str(db.REMINDERS[ID])
        create_file_path = PATH_EMAIL_SCRIPTS + "/" + daemon_name + ".py"

        f.create_email_script(db.REMINDERS[ID], db.REMINDERS[EMAIL], daemon_name)
        f.create_service(create_file_path, daemon_name)
        f.create_timer(reminder_timestamp, daemon_name)
        # f.execute_timer(daemon_name)
        db.REMINDERS[ID] += 1
        db.dump_reminders()

    elif main_menu_input == "2":
        if db.REMINDERS[LIST]:
            while True:
                if not db.REMINDERS[LIST]:
                    break
                valid_reminder_choice = []
                for index, reminder in enumerate(db.REMINDERS[LIST]):
                    index += 1
                    valid_reminder_choice.append(index)
                    print("[" + str(index) + "]", reminder.title)
                print("[" + str(len(db.REMINDERS[LIST]) + 1) + "]", "Go back")

                choose_reminder = f.input_to_int()
                if choose_reminder in valid_reminder_choice:
                    open_reminder(choose_reminder - 1)

                elif choose_reminder == len(db.REMINDERS[LIST]) + 1:
                    print("Going back")
                    break
                else:
                    print("error")
        else:
            print("There are no reminders")

    elif main_menu_input == "3":
        receiver_email = input("Receiver email: ")
        db.REMINDERS[EMAIL] = receiver_email
        print("Your reminders will be sent to email: " + receiver_email)
        db.dump_reminders()

    elif main_menu_input == "4":
        print("Exiting...")
        db.dump_reminders()
        break
    else:
        print("Invalid input")
