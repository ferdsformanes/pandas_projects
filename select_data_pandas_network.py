import pandas as pd
from netmiko import ConnectHandler

# -------------------------------
# Step 1: Read Excel File
# -------------------------------
df = pd.read_excel(r"C:\Users\user\Desktop\ftc\Topics\Python\Projects\sdwan\devices.xlsx")

# Strip column names and ensure all required columns are strings
df.columns = df.columns.str.strip() # run df.columns to see the space
df["hostname"] = df["hostname"].astype(str).str.strip() # run df["hostname"].iloc[0] to the space
df["username"] = df["username"].astype(str).str.strip() 
df["password"] = df["password"].fillna("").astype(str).str.strip() # run df["password"].iloc[1] to the space
df["device_type"] = df["device_type"].astype(str).str.strip()

print("DataFrame loaded:")
print(df, "\n")

# -------------------------------
# Step 2: Select Needed Columns
# -------------------------------
df = df[["device_type", "hostname", "username", "password"]]

# -------------------------------
# Step 3: Loop through devices
# -------------------------------
for index, row in df.iterrows():
    print(type(row))
    print(row)
    if row["hostname"] == "":
        print("Skipping a device with empty hostname...\n")
        continue

    device = {
        "device_type": row["device_type"],
        "host": row["hostname"],
        "username": row["username"],
        "password": row["password"],
    }

    print(f"Connecting to {device['host']} via Telnet...")

    try:
        connection = ConnectHandler(**device)
        try:
            # Execute command based on device type
            if device["device_type"] == "cisco_ios_telnet":
                output = connection.send_command("show ip interface brief")
            elif device["device_type"] == "juniper_junos_telnet":
                output = connection.send_command("show bgp summary")
            else:
                print(f"Unknown device type {device['device_type']}, skipping...")
                continue

            # Save output to file (current working directory)
            filename = f"{device['host']}_output.txt"
            with open(filename, "w") as f:
                f.write(output)

            print(f"Saved output to {filename}\n")

        finally:
            # Ensure disconnection always happens
            connection.disconnect()

    except Exception as e:
        print(f"Failed to connect to {device['host']}: {e}")
        print("Skipping this device and continuing...\n")