from main_dir.pickle_db import data_handler as db
import functions.funcs as r_funcs
import reminder_class

#  CONSTANTS
LIST = db.LIST  # This is the key for the dict
ID = db.ID      # This is the key for the dict

while True:
    print("\n[1] Create reminder\n[2] View reminders\n[3] Exit")
    main_menu_input = input(": ")

    if main_menu_input == "1":
        reminder_title = input("Reminder title: ")
        print("\nThis is a multi-line input for your reminder text")
        reminder_text = r_funcs.multiline_input()
        reminder_timestamp = r_funcs.create_reminder_timestamp()

        reminder_object = reminder_class.Reminder(reminder_title, reminder_text, reminder_timestamp, db.REMINDERS[ID])
        db.REMINDERS[ID] += 1
        db.REMINDERS[LIST].append(reminder_object)

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

                choose_to_do = r_funcs.input_to_int()
                if choose_to_do in valid_reminder_choice:
                    r_funcs.open_to_do(choose_to_do - 1)

                elif choose_to_do == len(db.REMINDERS[LIST]) + 1:
                    print("Going back")
                    break
                else:
                    print("error")
        else:
            print("There are no reminders")

    elif main_menu_input == "3":
        print("Exiting...")
        db.dump_reminders()
        break
    else:
        print("Invalid input")