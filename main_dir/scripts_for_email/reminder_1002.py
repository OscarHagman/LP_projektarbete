#!/usr/bin/python3.8
import os  # THIS IS NEW
import smtplib

# NEEDS TO BE CUSTOMIZABLE
REMINDER_ID = 1002
receiver_email = "oscar.leslie.hagman@gmail.com"

sender_email = "oscars.reminder.bot@gmail.com"
password = "devops2020"
port = 587

title = "testing self destruct"
text = "testing self destruct\n\nRegards, ORB"

message = "Subject: " + title + "\n\n" + text

try:
    server = smtplib.SMTP(host='smtp.gmail.com', port=port)
    server.starttls()
    server.login(sender_email, password)

    server.sendmail(sender_email, receiver_email, message)
    server.quit()
except Exception as e:
    print("ERROR:", e)

# EVERYTHING BELOW THIS LINE IS NEW
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
PATH_EMAIL_SCRIPTS = "/home/ianertson/workspace/LP_projektarbete/main_dir/scripts_for_email"
d_python = daemon_name + ".py"
print("sudo rm " + PATH_EMAIL_SCRIPTS + "/" + d_python)
os.system("sudo rm " + PATH_EMAIL_SCRIPTS + "/" + d_python)
