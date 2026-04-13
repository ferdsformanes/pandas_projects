# -----------------------------------------------
# Pandas Sorting Data (sort_values, sort_index)
# -----------------------------------------------

import pandas as pd

# -----------------------------------------------
# WHY SORT DATA?
# -----------------------------------------------
# 1. Find lowest/highest values quickly
# 2. Make data easier to read
# 3. Prepare data for analysis
# 4. Group related values together

# -----------------------------------------------
# CREATE SAMPLE DATAFRAME
# -----------------------------------------------
data = {
    "device_id": [3, 1, 2],
    "device_name": ["Router", "Switch", "Firewall"],
    "ip_address": ["192.168.1.1", "192.168.1.2", "192.168.1.3"],
    "price": [750, 1000, 500]
}

df = pd.DataFrame(data)
print(df)

# -----------------------------------------------
# sort_values() - SORT BY COLUMN VALUES
# -----------------------------------------------

# Sort by price (ascending)
df.sort_values(by="price", inplace=True)
print(df)

# Sort by price (descending)
df.sort_values(by="price", ascending=False, inplace=True)
print(df)

# Sort by multiple columns
df.sort_values(by=["price", "device_name"], inplace=True)
print(df)

# -----------------------------------------------
# RESET INDEX (IMPORTANT AFTER sort_values)
# -----------------------------------------------
df.reset_index(drop=True, inplace=True)
print(df)

# -----------------------------------------------
# sort_index() (ROW INDEX SORTING)
# -----------------------------------------------
# First, create a messy index to make the effect visible
df.index = [10, 5, 20]
print(df)

# Now sort by index
df.sort_index(inplace=True)
print(df)

# -----------------------------------------------
# sort_index(axis=1) - SORT COLUMN NAMES
# -----------------------------------------------
df.sort_index(axis=1, inplace=True)
print("\nColumns sorted alphabetically:")
print(df)

# -----------------------------------------------
# KEY TAKEAWAYS
# -----------------------------------------------
# 1. sort_values() → sorts based on column values
# 2. sort_index() → sorts based on row index
# 3. sort_index(axis=1) → sorts column names
# 4. inplace=True → modifies original DataFrame
# 5. reset_index(drop=True) → resets index after sorting