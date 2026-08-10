import sys
import subprocess
import time

SSID = "SIM7600NA"
PASSWORD = "G9YDrfVdeavE"

# for 2 minutes check if wifi is connected
for i in range(60):
    result = subprocess.check_output(["nmcli","-t"])
    for line in result.split(b"\n"):
        if b"wlan0: connected" in line:
            print(line.decode())
            sys.exit(0)
    
    print(result.decode())
    print("Indicates we're disconnected from wifi")
    time.sleep(1)


print("Starting a wifi hotspot! SSID",SSID+", password",PASSWORD)
# Start a wifi hotspot!
subprocess.run(["sudo", "nmcli", "device", "wifi", "hotspot", "ssid", SSID, "password", PASSWORD, "ifname", "wlan0"])
