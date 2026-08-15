Monitor for WIFI connections and start hotspot if not connected.

# Installation
Run `crontab -e` to add the line
```
*/2 * * * * /usr/bin/python /home/gadget/headless/headless.py $SSID $WPA_PASSWORD>> /home/gadget/headless/headless.log 2>&1
```
to start monitoring and logging.
`$SSID` should specify the ID for the wifi hotspot, that will start if disconnected from WIFI.
`$WPA_PASSWORD` should specify the password for the wifi hotspot

# Updating wifi credentials
After reconnecting to the hotspot presented by this raspberry pi, it can be assigned to join a new wifi network with
```
raspi-config
```

