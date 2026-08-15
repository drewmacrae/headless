import argparse
import sys
import subprocess
import time

SSID = "SIM7600NA"
PASSWORD = "G9YDrfVdeavE"

parser = argparse.ArgumentParser()
parser.add_argument("ssid",help="SSID for wifi hotspot that will start if disconnected from WIFI",default=SSID)
parser.add_argument("password",help="Passwrod for hotspot",default=PASSWORD)
args = parser.parse_args()

# for 1 minute check if wifi is connected
for i in range(60):
    result = subprocess.check_output(["nmcli","-t"])
    for line in result.split(b"\n"):
        if b"wlan0: connected" in line:
            print(line.decode())
            sys.exit(0)
    
    print(result.decode())
    print("Indicates we're disconnected from wifi")
    time.sleep(1)


print("Starting a wifi hotspot! SSID",args.ssid+", password",args.password)
# Start a wifi hotspot!
subprocess.run(["sudo", "nmcli", "device", "wifi", "hotspot", "ssid", args.ssid, "password", args.password, "ifname", "wlan0"])
