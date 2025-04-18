# uptime_checker.py

import requests
from datetime import datetime

# Replace this with any website you'd like to check
url = "https://www.google.com"

try:
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
        status = "UP"
    else:
        status = "DOWN"
except requests.RequestException:
    status = "DOWN"

# Log the result
with open("uptime_log.txt", "a") as log:
    log.write(f"{datetime.now()}: {url} is {status}\n")

print(f"{url} is {status}")
