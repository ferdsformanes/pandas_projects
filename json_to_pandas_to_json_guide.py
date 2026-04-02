# -----------------------------------------------
# JSON → Python Object → Pandas DataFrame → JSON
# -----------------------------------------------

import pandas as pd
import requests
import json
import urllib3

# -----------------------------------------------
# Disable SSL Warnings (Lab Environment)
# -----------------------------------------------

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# -----------------------------------------------
# Login to SD-WAN API (Session-Based Authentication)
# -----------------------------------------------

HOST = "https://sandbox-sdwan-2.cisco.com"
USERNAME = "devnetuser"
PASSWORD = "RG!_Yw919_83"

session = requests.Session()

login_url = f"{HOST}/j_security_check"
payload = {
    "j_username": USERNAME,
    "j_password": PASSWORD
}
response = session.post(login_url, data=payload, verify=False)

if response.status_code != 200 or "JSESSIONID" not in session.cookies:
    raise Exception("Login failed!")

print("Logged in successfully")
print("JSESSIONID:", session.cookies.get("JSESSIONID"))

# -----------------------------------------------
# Get Devices (JSON from API)
# -----------------------------------------------

devices_url = f"{HOST}/dataservice/device"
response = session.get(devices_url, verify=False)

if response.status_code != 200:
    raise Exception(f"Failed to retrieve devices: {response.status_code}")

# -----------------------------------------------
# Inspect RAW JSON (Before Conversion) & Save Pretty
# -----------------------------------------------

print(type(response.text))   # str (raw JSON)

# Parse the raw JSON string
parsed_json = json.loads(response.text)

# Pretty-printing in terminal
print(json.dumps(parsed_json, indent=4))  

# Save pretty JSON to file for inspection
with open("raw_sdwan_response.json", "w") as f:
    json.dump(parsed_json, f, indent=4)   

# -----------------------------------------------
# Convert JSON → Python Object (dict)
# -----------------------------------------------

data = response.json()

print(type(data))   # dict
print(data.keys())  # inspect top-level keys

# -----------------------------------------------
# Extract Device List
# -----------------------------------------------

devices = data.get("data", [])
print(type(devices))      # list
print(len(devices))       # number of devices
print(devices[0])         # inspect first device

# -----------------------------------------------
# Python Object → Pandas DataFrame
# -----------------------------------------------

df = pd.json_normalize(devices)
print(df.head())

# -----------------------------------------------
# Select / Clean Columns
# -----------------------------------------------

df = df[["host-name", "deviceId", "reachability"]]

print(df.head())

# -----------------------------------------------
# DataFrame -> Excel
# -----------------------------------------------

df.to_excel("sdwan_devices.xlsx", index=False)

# -----------------------------------------------
# DataFrame → JSON
# -----------------------------------------------

json_output = df.to_json(orient="records", indent=4)

print(json_output)

# -----------------------------------------------
# Save JSON to File
# -----------------------------------------------

with open("sdwan_devices.json", "w") as f:
    f.write(json_output)

# -----------------------------------------------
# KEY TAKEAWAYS
# -----------------------------------------------

# session.post() → login (JSESSIONID)
# session.get() → retrieve API data
# response.text → raw JSON string (before conversion)
# json.loads() → manually parse JSON
# response.json() → JSON → Python dict
# dict/list → DataFrame
# DataFrame → structured analysis
# df.to_json() → DataFrame → JSON