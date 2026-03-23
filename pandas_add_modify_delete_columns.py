import pandas as pd

# -------------------------------
# Step 1: Load Excel File
# -------------------------------
print("Step 1: Load Excel File")
df = pd.read_excel("devices.xlsx")
df.columns = df.columns.str.strip()
print(df)
print()

# -------------------------------
# Step 2: Add New Columns
# -------------------------------
print("Step 2: Add New Columns")
df[["status", "location"]] = ["up", "PH"]
print(df)
print()

# -------------------------------
# Step 3: Add New Row
# -------------------------------
print("Step 3: Add New Row")
df.loc[len(df)] = ["router3", "admin", "admin123", "cisco_ios_telnet", "up", "PH"]
print(df)
print()

# -------------------------------
# Step 4: Modify values in a Column
# -------------------------------
print("Step 4: Modify Column (hostname to uppercase)")
df["hostname"] = df["hostname"].str.lower()
print(df)
print()

# -------------------------------
# Step 5: Delete Columns
# -------------------------------
print("Step 5: Delete Columns")
# Option 1: Delete a single column df = df.drop(columns= "status") 
# Option 2: Delete multiple columns # df = df.drop(["status", "ip"], axis=1) 
# Option 3: Delete column using del # del df["status"]

# -------------------------------
# Step 6: Delete Rows
# -------------------------------
print("Step 6: Delete Last Row")
df = df.iloc[:-1]
print(df)