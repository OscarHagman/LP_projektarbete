#!/usr/bin/python3.8
import os
import smtplib
from pickle_db import data_handler as db

handler = db.ReminderHandler()
handler.load_reminder()

#  CONSTANTS
LIST = db.LIST  # This is the key for the dict
ID = db.ID  # This is the key for the dict

# NEEDS TO BE CUSTOMIZABLE
REMINDER_ID = 1004
receiver_email = "oscar.leslie.hagman@gmail.com"

sender_email = "oscars.reminder.bot@gmail.com"
password = "devops2020"
port = 587

title = ""
text = ""
for reminder in handler.REMINDERS[LIST]:
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

