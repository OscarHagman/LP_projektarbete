echo Enter daemon to test
read daemon_name

service="${daemon_name}.service"
timer="${daemon_name}.timer"
python="${daemon_name}.py"

sudo mv $service /etc/systemd/system
sudo mv $timer /etc/systemd/system
chmod +x ./main_dir/scripts_for_email/$python

sudo systemctl daemon-reload
sudo systemctl enable $timer
sudo systemctl start $timer
