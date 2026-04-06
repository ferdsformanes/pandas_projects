# -----------------------------------------------
# Merging DataFrames in Pandas
# (Inner, Left, Right, Outer Joins and Column Mapping)
# -----------------------------------------------

import pandas as pd

# -----------------------------------------------
# Step 1: Load Data from Excel Files
# -----------------------------------------------

df_devices = pd.read_excel("network_devices.xlsx")
df_locations = pd.read_excel("device_locations.xlsx")
print(df_devices)
print(df_locations)


# -----------------------------------------------
# Step 2: Basic Merge (Inner Join - DEFAULT)
# -----------------------------------------------
# INNER JOIN is the DEFAULT behavior of pd.merge()
# If "how" is not specified, Pandas uses INNER JOIN
# Keeps only devices present in BOTH DataFrames
df_inner = pd.merge(df_devices, df_locations, on="device_id")
# Equivalent to:
# df_inner = pd.merge(df_devices, df_locations, on="device_id", how="inner")
print(df_inner)


# -----------------------------------------------
# Step 3: Left Join
# -----------------------------------------------
# LEFT JOIN keeps all devices from df_devices
# and matches locations if available
df_left = pd.merge(df_devices, df_locations, on="device_id", how="left")
print(df_left)


# -----------------------------------------------
# Step 4: Right Join
# -----------------------------------------------
# RIGHT JOIN keeps all rows from df_locations
# and matches devices if available
df_right = pd.merge(df_devices, df_locations, on="device_id", how="right")
print(df_right)


# -----------------------------------------------
# Step 5: Outer Join
# -----------------------------------------------
# OUTER JOIN keeps all rows from BOTH DataFrames
df_outer = pd.merge(df_devices, df_locations, on="device_id", how="outer")
print(df_outer)


# -----------------------------------------------
# Step 6: Merge on Different Column Names
# -----------------------------------------------
# Example: merging vendor info stored with a different column name
df_vendors = pd.read_excel("device_vendors.xlsx")  
df_merge_diff = pd.merge(df_devices, df_vendors, left_on="device_id", right_on="dev_id")
print(df_merge_diff)


# -----------------------------------------------
# Step 7: Export Merged Data to Excel
# -----------------------------------------------
# Save the merged DataFrame 
df_inner.to_excel("network_devices_inner_join_merged.xlsx", index=False)


# -----------------------------------------------
# KEY TAKEAWAYS
# -----------------------------------------------
# 1. pd.merge() is used to combine DataFrames
# 2. "on" specifies the common column to merge
# 3. INNER join = DEFAULT (only matching rows from both DataFrames)
# 4. LEFT join = all rows from the left DataFrame
# 5. RIGHT join = all rows from the right DataFrame
# 6. OUTER join = all rows from both DataFrames
# 7. Use left_on and right_on if column names differ
