#!/usr/bin/python3.8
import os
import smtplib
from pickle_db import data_handler as db

#  CONSTANTS
LIST = db.LIST  # This is the key for the dict
ID = db.ID  # This is the key for the dict

# NEEDS TO BE CUSTOMIZABLE
REMINDER_ID = 1003
receiver_email = ""

sender_email = "oscars.reminder.bot@gmail.com"
password = "devops2020"
port = 587

title = ""
text = ""
for reminder in db.REMINDERS[LIST]:
    if reminder.reminder_id == REMINDER_ID:
        title = reminder.title
        text = reminder.text
    else:
        title = "ERROR"
        text = "Couldn't find REMINDER_ID:", REMINDER_ID
message = "Subject: " + title + "\n\n" + text

try:
    server = smtplib.SMTP(host='smtp.gmail.com', port=port)
    server.starttls()
    server.login(sender_email, password)

    server.sendmail(sender_email, receiver_email, message)
    server.quit()
except Exception as e:
    print("ERROR:", e)

# !!!EVERYTHING BELOW THIS LINE IS NEW!!!
daemon_name = "reminder_" + str(REMINDER_ID)
d_service = daemon_name + ".service"
d_timer = daemon_name + ".timer"

systemd_path = "/etc/systemd/system/"
lib_systemd_path = "/etc/systemd/system/"

os.system("sudo systemctl stop " + d_timer)
os.system("sudo systemctl disable " + d_timer)
os.system("sudo rm " + systemd_path + d_timer)
os.system("sudo rm " + lib_systemd_path + d_timer)

os.system("sudo systemctl stop " + d_service)
os.system("sudo systemctl disable " + d_service)
os.system("sudo rm " + systemd_path + d_service)
os.system("sudo rm " + lib_systemd_path + d_service)

# SELF DESTRUCT
PATH_EMAIL_SCRIPTS = "/home/oscar/oscars_projektarbete/main_dir/"
d_python = daemon_name + ".py"
print("sudo rm " + PATH_EMAIL_SCRIPTS + "/" + d_python)
os.system("sudo rm " + PATH_EMAIL_SCRIPTS + "/" + d_python)
