## How program works
E.g. 
./cpu_usage.py -M 20 -T 10
-M (memory check, if memory is higher than e.g. 20, it will beep)
-T (timer, 10 = 10 sec, its required).

cpu_usage.rapport.txt is used to logg information:
- If app is running (beep once)
- PID, Name, Memory
- Was entered memory higher or lower than memory (higher = beep sound)

# Access to root
sudo su -

sudo nano /etc/systemd/system/cpu_usage_service
sudo nano cpu_usage.py

# Files and path
- /home/kevin/cpu_usage_rapport.txt
- /home/kevin/cpu_usage.py
- /etc/systemd/system/cpu_usage_service

# Reload daemon
- sudo systemctl daemon-reload

# Enable service
- sudo systemctl enable cpu_usage.service

# Start service
- sudo systemctl start cpu_usage.service

# Stop service
- sudo systemctl stop cpu_usage.service

# Restart service
- sudo systemctl restart cpu_usage.service

# Check status of service
- sudo systemctl status cpu_usage.service

# Disable service
- sudo systemctl disable cpu_usage.service
