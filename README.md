# Reminder application for linux based systems (systemd)

This application was made for a school project.
It's purpose is to let the user have custom reminders sent to their email at a specific date and time.

For this application to work you need:
Python 3.8.
Git.
Low expectations.

### How to install:
1. git clone to the desired directory
2. Run the install.sh script by typing in ". install.sh" in your terminal. (You have to be in the LP_projektarbete directory for it to work). And that's all!

### How to use:
The install.sh script creates a command after what you, the user, have entered for it to be. So to run the program you simply just type in that command anywhere on the computer and it will be executed. (Provided that you executed the install.sh script correctly, have a compatible OS, python 3.8 and don't tamper with the programs directory or any files in it)
##### [1] Create reminder  -  Lets you create a reminder with a title, text and a reminder date. Reminder date is when the email will be sent.
##### [2] View reminders  -  Prints out all your reminders and let you open them to either read or delete them. (However, the delete function doesn't actually work, trying to do so will crash the program)
##### [3] Set receiver email  -  Set what email you want to get your email sent to. You only have to do this once, unless you want to change what email you want your reminders will be sent to.
##### [4] Exit  -  Pretty self explanatory

The scripts that sends the email have code in them that are designed to self destruct after they have been executed. However, there is a bug where the self destruct code doesn't succeed in removing the reminder_xxxx.service file. So you will have to do that manually, unless you're ok with having a bunch of useless junk in your /etc/systemd/system directory.

Due to a lot, (and I really do mean A LOT), of unforeseeable problems and other hiccups with this project, I had a really limited time in finishing this application so that's why there are so many bugs in it.
