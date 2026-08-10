Monitor for WIFI connections and start hotspot if not connected.

# Installation
Run `crontab -e` to add the line
```
*/2 * * * * /usr/bin/python /home/pygu/headless/headless.py >> /home/pygu/headless/headless.log 2>&1
```
to start monitoring and logging

# Updating wifi credentials
After reconnecting to the hotspot presented by this raspberry pi, it can be assigned to join a new wifi network with
```
raspi-config
```

