def create_email_scripts(id_number, receiver_email) -> None:
    """
    Writes a custom and unique .py, .service and .timer file based on templates.
    The .py file opens the .pickle file, searches for a matching id number and attaches the title and text to the
    message that will be sent to the receiver_email address.

    The .service file will execute the .py file.

    The .timer file will execute the .service file at the given date & time

    :param id_number: Is used to locate correct data to send in the email and to create unique file names.
    :param receiver_email: Email address the .py file will send that data to.
    :param timestamp: Will set what date & time the .timer file will execute the .service file.
    """
    receiver_email = '"' + receiver_email + '"'  # Ads "" to the string so it gets represented as a string in the script
    create_file_path = SAVE_PYTHON_PATH + "/reminder_" + str(id_number) + ".py"  # Creates a unique file name
    with open(PATH_PYTHON_TEMPLATE, "r") as template:
        template_list = template.readlines()
    #  Removes the '\n' from the end of each element and ads the item into a new list
    edited_list = []
    for item in template_list:
        edited_item = item.strip("\n")
        edited_list.append(edited_item)

    # Find where the id and email variable is in the list and ads the custom value to them
    id_index = edited_list.index("REMINDER_ID")
    receiver_index = edited_list.index("receiver_email")
    edited_reminder_id = (edited_list[id_index] + " = " + str(id_number))
    edited_receiver_email = (edited_list[receiver_index] + " = " + receiver_email)

    #  Ads the edited id number and receiver email to correct variables in the script
    edited_list[id_index] = edited_reminder_id
    edited_list[receiver_index] = edited_receiver_email

    # Creates a new .py file in the given path and writes the custom script to the file
    with open(create_file_path, "w") as email_script:
        for line in edited_list:
            print(line, file=email_script)


def create_service(email_script_path):
    with open("/main_dir/scripts_for_email/TEMPLATES/service_template.cfg", "r") as template:
        template_list = template.readlines()
    #  Removes the '\n' from the end of each element and ads the item into a new list
    edited_list = []
    for item in template_list:
        edited_item = item.strip("\n")
        edited_list.append(edited_item)

    id_exec_start = edited_list.index("ExecStart=")
    edited_exec_start = (edited_list[id_exec_start] + email_script_path)
    edited_list[id_exec_start] = edited_exec_start

    #  Reverses the path to the script to execute, finds first slash index (which is the last slash)
    #  and saves everything beyond that except last 2 chars (which is 'py')
    slash_index = email_script_path[::-1].index("/")
    start = len(email_script_path) - slash_index
    file_name = email_script_path[start:-2]
    #  Creates path with the unique file_name.service
    create_file_path = "/etc/systemd/system/" + file_name + "service"

    # Creates a new .py file in the given path and writes the custom script to the file
    with open(create_file_path, "w") as service_file:
        for line in edited_list:
            print(line, file=service_file)


def create_timer(id_number):
    pass