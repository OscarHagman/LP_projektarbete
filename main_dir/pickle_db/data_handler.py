import sys
import pickle
import os
sys.path.append("main_dir/pickle_db")

PATH_TEMPLATES = PATH_PROJECT + "/main_dir/scripts_for_email/TEMPLATES"
PATH_PYTHON_TEMPLATE = PATH_TEMPLATES + "/python_template.cfg"
PATH_SERVICE_TEMPLATE = PATH_TEMPLATES + "/service_template.cfg"
PATH_TIMER_TEMPLATE = PATH_TEMPLATES + "/timer_template.cfg"
PICKLE_PATH = PATH_PROJECT + "/main_dir/pickle_db/reminders.pickle"

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


class ReminderHandler:

    def __init__(self):
        self.REMINDERS = {LIST: [], ID: ID_COUNTER, EMAIL: ""}


    def get_reminder(self, reminder_index):
        opened_reminder = self.REMINDERS[LIST][reminder_index]
        return opened_reminder


    def add_reminder(self,reminder_object):
        self.REMINDERS[LIST].append(reminder_object)


    def load_reminder(self):
        if not os.path.isfile(PICKLE_PATH):
            return
            
        if os.path.getsize(PICKLE_PATH) > 0:
            with open(PICKLE_PATH, "rb") as reminder_pickled:
                self.REMINDERS = pickle.load(reminder_pickled)


ID_COUNTER = 1001
#REMINDERS = {LIST: [], ID: ID_COUNTER, EMAIL: ""}


def dump_reminders(handler):
    #with  as reminder_pickled:
    pickle.dump(handler.REMINDERS, open(PICKLE_PATH, "wb"))
