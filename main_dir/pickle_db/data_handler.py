import pickle


class Reminder:

    def __init__(self, title, text, reminder_date, reminder_id):
        self.title = title
        self.text = text
        self.reminder_date = reminder_date
        self.reminder_id = reminder_id


#  KEYS
LIST = "reminder_key_list"
ID = "reminder_key_id"

ID_COUNTER = 1001
REMINDERS = {LIST: [], ID: ID_COUNTER}
PICKLE_PATH = "/home/oscar/oscars_projektarbete/main_dir/pickle_db/reminders.pickle"

try:
    with open(PICKLE_PATH, "rb") as reminder_pickled:
        REMINDERS = pickle.load(reminder_pickled)
except FileNotFoundError:
    pass


def dump_reminders():
    with open(PICKLE_PATH, "wb") as pickle_file:
        pickle.dump(REMINDERS, pickle_file)
