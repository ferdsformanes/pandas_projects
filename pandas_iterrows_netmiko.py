# -------------------------------
# Pandas iterrows + Network Automation (Simple Tutorial)
# -------------------------------

import pandas as pd
from netmiko import ConnectHandler

# -------------------------------
# Step 1: Load Excel File
# -------------------------------
df = pd.read_excel(r"C:\Users\user\Desktop\ftc\Topics\Python\Projects\sdwan\devices.xlsx")

# Clean column names and fill missing passwords
df.columns = df.columns.str.strip()
df["password"] = df["password"].fillna("")

# -------------------------------
# iterrows() Syntax
# -------------------------------
# for index, row in df.iterrows():
#     index -> row number (0, 1, 2, ...)
#     row   -> pandas Series (like a dictionary)
# Access values: row["column_name"]

# Example:
# for index, row in df.iterrows():
#     print(index, row["hostname"], row["device_type"])

# -------------------------------
# Step 2: Loop through rows and use Netmiko
# -------------------------------
for index, row in df.iterrows():

    # Access row values
    hostname = row["hostname"]
    username = row["username"]
    password = row["password"]
    device_type = row["device_type"]

    # Skip empty hostnames
    if hostname == "":
        continue

    print(f"\nProcessing device {hostname} ({device_type})")

    # Build device dictionary for Netmiko
    device = {
        "device_type": device_type,
        "host": hostname,
        "username": username,
        "password": password,
    }

    # Connect and run a command
    try:
        connection = ConnectHandler(**device)
        print(f"Connected to {hostname}")

        # Example commands
        if "cisco" in device_type:
            output = connection.send_command("show ip interface brief")
        elif "juniper" in device_type:
            output = connection.send_command("show interfaces terse")
        else:
            output = connection.send_command("show version")

        # Print preview
        print(output[:200])

    except Exception as e:
        print(f"Failed to connect to {hostname}: {e}")

    finally:
        try:
            connection.disconnect()
            print(f"Disconnected from {hostname}")
        except:
            pass