import pickle

#  PATHS
PATH_PROJECT = "/home/oscar/oscars_projektarbete"
PATH_EMAIL_SCRIPTS = PATH_PROJECT + "/main_dir/scripts_for_email/"
PATH_TEMPLATES = PATH_EMAIL_SCRIPTS + "/TEMPLATES"
PATH_PYTHON_TEMPLATE = PATH_TEMPLATES + "/python_template.cfg"
PATH_SERVICE_TEMPLATE = PATH_TEMPLATES + "/service_template.cfg"
PATH_TIMER_TEMPLATE = PATH_TEMPLATES + "/timer_template.cfg"

#  KEYS
LIST = "reminder_key_list"
ID = "reminder_key_id"
EMAIL = "reminder_key_receiver_email"


class Reminder:

    def __init__(self, title, text, reminder_date, reminder_id):
        self.title = title
        self.text = text
        self.reminder_date = reminder_date
        self.reminder_id = reminder_id


ID_COUNTER = 1001
REMINDERS = {LIST: [], ID: ID_COUNTER, EMAIL: ""}
PICKLE_PATH = "/home/oscar/oscars_projektarbete/main_dir/pickle_db/reminders.pickle"

try:
    with open(PICKLE_PATH, "rb") as reminder_pickled:
        REMINDERS = pickle.load(reminder_pickled)
except FileNotFoundError:
    pass


def dump_reminders():
    with open(PICKLE_PATH, "wb") as pickle_file:
        pickle.dump(REMINDERS, pickle_file)
