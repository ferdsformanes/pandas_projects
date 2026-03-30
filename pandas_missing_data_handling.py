# -----------------------------------------------
# How Pandas Handles Missing Data
# (None vs pd.NA vs Empty Strings vs null)
# -----------------------------------------------

import pandas as pd
import json

# -----------------------------------------------
# Create Example Data
# -----------------------------------------------

data = {
    "col": ["text", "", None, pd.NA]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
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

print("\nMissing Value Mask (True = missing):")
print(df.isna())

print("\nCount of Missing Values per Column:")
print(df.isna().sum())


# -----------------------------------------------
# Key Concept
# -----------------------------------------------
# None  → treated as missing
# pd.NA → treated as missing
# ""    → NOT treated as missing
# null  → becomes None → treated as missing


# -----------------------------------------------
# Fix: Convert Empty Strings to Missing Values
# -----------------------------------------------

df = df.replace("", pd.NA)

print("\nAfter Converting Empty Strings to pd.NA:")
print(df.isna().sum())


# -----------------------------------------------
# Fill Missing Values
# -----------------------------------------------

df["col"] = df["col"].fillna("Unknown")

print("\nAfter Filling Missing Values:")
print(df)


# -----------------------------------------------
# KEY TAKEAWAYS
# -----------------------------------------------
# None and pd.NA are considered missing values
# JSON null becomes None in Python
# Empty strings ("") are NOT missing by default
# Use replace("", pd.NA) to handle empty strings
# Use fillna() to fill missing values