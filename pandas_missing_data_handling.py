# -----------------------------------------------
# How Pandas Handles Missing Data
# (Handling None, pd.NA, Empty Strings, and JSON null in Pandas)
# -----------------------------------------------

import pandas as pd
import json

# -----------------------------------------------
# Load Data from Excel File
# -----------------------------------------------

df = pd.read_excel("sdwan_devices.xlsx")
print(df)


# -----------------------------------------------
# Simulating JSON null values
# -----------------------------------------------

# JSON 'null' becomes Python None when loaded
json_data = '[{"col": "text"}, {"col": null}]'
df_json = pd.DataFrame(json.loads(json_data))

print("\nDataFrame from JSON (null → None):")
print(df_json)


# -----------------------------------------------
# Detect Missing Values
# -----------------------------------------------

print(df.isna())
print(df.isna().sum())


# -----------------------------------------------
# Fix: Convert Empty Strings to Missing Values
# -----------------------------------------------

# Replace empty strings across ALL columns
df = df.replace(r'^\s*$', pd.NA, regex=True)
print(df.isna())


# -----------------------------------------------
# Fill Missing Values
# -----------------------------------------------

# Fill missing values (generic approach for demo)
df = df.fillna("Unknown")
print(df)


# -----------------------------------------------
# Export Data to Excel File
# -----------------------------------------------

df.to_excel("sdwan_devices_cleaned.xlsx", index=False)


# -----------------------------------------------
# KEY TAKEAWAYS
# -----------------------------------------------
# None and pd.NA are considered missing values
# JSON null becomes None in Python
# Empty strings ("") are NOT missing by default
# Use replace(r'^\s*$', pd.NA, regex=True) to handle empty strings
# Use fillna() to fill missing values