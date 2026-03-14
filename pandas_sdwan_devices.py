# How to Convert API JSON Data to Excel Using Pandas (Python Tutorial)

import json
import requests
import urllib3
import pandas as pd

# Ignore SSL warnings (self-signed cert)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- Configuration ---
HOST = "https://sandbox-sdwan-2.cisco.com"
USERNAME = "devnetuser"
PASSWORD = "RG!_Yw919_83"

# --- Functions ---
def login():
    """Authenticate and return a session with JSESSIONID."""
    session = requests.Session()
    login_url = f"{HOST}/j_security_check"
    payload = {"j_username": USERNAME, "j_password": PASSWORD}
    response = session.post(login_url, data=payload, verify=False)
    if response.status_code != 200 or "JSESSIONID" not in session.cookies:
        raise Exception("Login failed!")
    print("✅ Login successful.")
    return session


def get_devices(session):
    """Retrieve devices from SD-WAN Manager."""
    devices_url = f"{HOST}/dataservice/device"
    response = session.get(devices_url, verify=False)
    if response.status_code != 200:
        raise Exception("Failed to retrieve devices")
    return response.json() # Convert API JSON response into a Python dictionary


# --- Interactive IPython / Jupyter Steps ---

# Step 1: Login
session = login()

# Step 2: Get raw JSON data
devices = get_devices(session)

# print(json.dumps(devices, indent=4))
#  devices.keys()

# Step 3: Convert list of dictionaries into a flat Pandas DataFrame
df = pd.json_normalize(devices["data"]) # pd.json_normalize flattens nested JSON automatically

df.head()  # Only show first 5 rows

# Step 4: Select important columns
# df.columns  # Check available columns
df = df[["host-name", "deviceId", "device-type", "system-ip", "reachability"]]

# Step 5: Sort by hostname
df = df.sort_values(by="host-name")

# Step 6: Filter example (only reachable devices)
reachable_devices = df[df["reachability"] == "reachable"]

# Step 7: Export to Excel
excel_file = "sdwan_devices.xlsx"
df.to_excel(excel_file, index=False)
