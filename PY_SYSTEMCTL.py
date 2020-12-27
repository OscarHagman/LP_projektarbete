import os

daemon_name = input("Enter daemons to test: ")
d_service = daemon_name + ".service"
d_timer = daemon_name + ".timer"
d_python = daemon_name + ".py"

systemd_path = "/etc/systemd/system"
# os.system("sudo mv " + d_service + " " + systemd_path)
# os.system("sudo mv " + d_timer + " " + systemd_path)
os.system("chmod +x ./main_dir/scripts_for_email/" + d_python)

os.system("systemctl daemon-reload")
os.system("systemctl enable " + d_timer)
os.system("systemctl start " + d_timer)
