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

# -----------------------------------------------
# Create Sample DataFrame
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
# sort_values() - Sort by column values
# -----------------------------------------------
# Sort by price (ascending by default)
df_sorted = df.sort_values(by="price")

# Notice: index stays from original DataFrame
print(df_sorted)

# Sort by price descending
df_sorted_desc = df.sort_values(by="price", ascending=False)

print(df_sorted_desc)

# -----------------------------------------------
# Sort by multiple columns
# -----------------------------------------------
df_multi_sort = df.sort_values(by=["price", "device_name"])

print(df_multi_sort)

# -----------------------------------------------
# Sort by IP address (string-based sorting)
# -----------------------------------------------
df_ip_sorted = df.sort_values(by="ip_address")

print(df_ip_sorted)

# -----------------------------------------------
# Reset index after sorting (common practice)
# -----------------------------------------------
df_clean = df.sort_values(by="price").reset_index(drop=True)

print(df_clean)

# -----------------------------------------------
# sort_index() - Sort by index
# -----------------------------------------------
df_index_sorted = df_sorted.sort_index()

print(df_index_sorted)

# -----------------------------------------------
# sort_index(axis=1) - Sort columns
# -----------------------------------------------
df_column_sorted = df.sort_index(axis=1)

print(df_column_sorted)

# -----------------------------------------------
# KEY TAKEAWAYS
# -----------------------------------------------
# 1. sort_values() → sorts data based on column values
# 2. sort_index() → sorts based on index (rows)
# 3. sort_index(axis=1) → sorts column names
# 4. ascending=False → descending order
# 5. You can sort by multiple columns
# 6. reset_index() → fixes messy index after sorting