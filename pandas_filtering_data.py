# -----------------------------------------------
# Filtering Data in Pandas (Boolean Indexing)
# -----------------------------------------------

# -----------------------------------------------
# WHY FILTER DATA?
# -----------------------------------------------
# 1. Find specific rows quickly
# 2. Focus only on relevant data
# 3. Clean and analyze datasets
# 4. Extract insights from large data

# -----------------------------------------------
# Import pandas library
# -----------------------------------------------
import pandas as pd

# -----------------------------------------------
# CREATE SAMPLE DATAFRAME
# -----------------------------------------------
data = {
    "device_id": [3, 1, 2, 4],
    "device_name": ["Router", "Switch", "Firewall", "Router"],
    "ip_address": ["192.168.1.1", "192.168.1.2", "192.168.1.3", "192.168.1.4"],
    "price": [750, 1000, 500, 600]
}

df = pd.DataFrame(data)
print(df)

# -----------------------------------------------
# BASIC FILTERING (Single Condition)
# -----------------------------------------------

# Filter devices with price greater than 600
filtered_df = df[df["price"] > 600]
print(filtered_df)

# -----------------------------------------------
# MULTIPLE CONDITIONS (AND - &)
# -----------------------------------------------

# Price > 600 AND device_name is Router
filtered_df = df[(df["price"] > 600) & (df["device_name"] == "Router")]
print(filtered_df)

# -----------------------------------------------
# MULTIPLE CONDITIONS (OR - |)
# -----------------------------------------------

# Price > 900 OR device_name is Firewall
filtered_df = df[(df["price"] > 900) | (df["device_name"] == "Firewall")]
print(filtered_df)

# -----------------------------------------------
# NOT CONDITION (~)
# -----------------------------------------------

# Exclude Routers
filtered_df = df[~(df["device_name"] == "Router")]
print(filtered_df)

# -----------------------------------------------
# USING .isin() METHOD
# -----------------------------------------------

# Filter specific device types
filtered_df = df[df["device_name"].isin(["Router", "Switch"])]
print(filtered_df)

# -----------------------------------------------
# FILTER AND RESET INDEX (COMMON PRACTICE)
# -----------------------------------------------

filtered_df = df[df["price"] > 600].reset_index(drop=True)
print(filtered_df)

# -----------------------------------------------
# KEY TAKEAWAYS
# -----------------------------------------------
# 1. Filtering = selecting rows based on conditions
# 2. Use [] with conditions for filtering
# 3. & = AND, | = OR, ~ = NOT
# 4. .isin() helps match multiple values
# 5. reset_index(drop=True) cleans index after filtering