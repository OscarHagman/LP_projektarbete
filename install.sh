touch run.sh
file_name=$"run.sh"
echo Enter the desired command name for the shell script
read command_name

# Goes on top of command
cmd_line1="#!/bin/bash\n"
path=$(echo $(pwd))
cmd_line2="sudo python3 ${path}/reminder.py"

command_ontop="${cmd_line1}${cmd_line2}"

echo -e "${command_ontop}" | cat - $file_name > temp && mv temp $file_name
chmod +x $file_name
sudo mv $file_name /usr/local/bin/$command_name

# Goes on top of db.py
PATH_value="'${path}'"
db_line1="import sys\nimport pickle\nimport os\nsys.path.append('main_dir/pickle_db')\n"
db_line2="\n#  PATHS\nPATH_PROJECT = ${PATH_value}\n"

db_ontop="${db_line1}${db_line2}"

db_file_name=$"${path}/main_dir/pickle_db/data_handler.py"
echo -e "${db_ontop}" | cat - $db_file_name > temp && mv temp $db_file_name

echo "Installation complete. You can now enter ${command_name} anywhere on the computer to run the program"
