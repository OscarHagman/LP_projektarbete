import os

daemon_name = input("Daemon name: ")
d_service = daemon_name + ".service"
d_timer = daemon_name + ".timer"

systemd_path = "/etc/systemd/system/"
lib_sysd_path = "/etc/systemd/system/"

os.system("sudo systemctl stop " + d_timer)
os.system("sudo systemctl disable " + d_timer)
os.system("sudo rm " + d_timer)
os.system("sudo rm " + lib_sysd_path + d_timer)

os.system("sudo systemctl stop " + d_service)
os.system("sudo systemctl disable " + d_service)
os.system("sudo rm " + d_service)
os.system("sudo rm " + lib_sysd_path + d_service)

