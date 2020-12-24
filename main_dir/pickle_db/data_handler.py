import pickle

#  KEYS
LIST = "reminder_key_list"
ID = "reminder_key_id"

REMINDER_ID = 1001
REMINDERS = {LIST: [], ID: REMINDER_ID}
PICKLE_PATH = "/home/oscar/oscars_projektarbete/main_dir/pickle_db/reminders.pickle"

try:
    with open(PICKLE_PATH, "rb") as reminder_pickled:
        REMINDERS = pickle.load(reminder_pickled)
except FileNotFoundError:
    pass


def dump_reminders():
    with open(PICKLE_PATH, "wb") as pickle_file:
        pickle.dump(REMINDERS, pickle_file)
