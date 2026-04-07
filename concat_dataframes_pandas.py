# -----------------------------------------------
# Pandas Concat Explained (Combine DataFrames Easily)
# -----------------------------------------------

import pandas as pd

# -----------------------------------------------
# Step 1: Create Sample DataFrames
# -----------------------------------------------
df1 = pd.DataFrame({
    "device_id": [1, 2],
    "device_name": ["Router", "Switch"]
})

df2 = pd.DataFrame({
    "device_id": [3, 4],
    "device_name": ["Firewall", "Access Point"]
})

print(df1)
print(df2)

# -----------------------------------------------
# Step 2: Row-wise Concatenation (axis=0) - DEFAULT
# -----------------------------------------------
# Stacks DataFrames vertically (adds rows)
df_rows = pd.concat([df1, df2])
print(df_rows)

# -----------------------------------------------
# Step 3: Reset Index (ignore_index=True)
# -----------------------------------------------
# Fixes duplicate index after stacking
df_rows_reset = pd.concat([df1, df2], ignore_index=True)
print(df_rows_reset)

# -----------------------------------------------
# Step 4: Column-wise Concatenation (axis=1)
# -----------------------------------------------
# Combines DataFrames side-by-side (adds columns)
df_cols = pd.concat([df1, df2], axis=1)
print(df_cols)

# -----------------------------------------------
# Step 5: Different Columns (NaN Values)
# -----------------------------------------------
df3 = pd.DataFrame({
    "device_id": [5, 6],
    "ip_address": ["192.168.1.1", "192.168.1.2"]
})

# Missing columns will be filled with NaN
df_mixed = pd.concat([df1, df3], ignore_index=True)
print(df_mixed)

# -----------------------------------------------
# Step 6: KEY DIFFERENCE (MERGE vs CONCAT)
# -----------------------------------------------
# CONCAT = stacking or combining DataFrames
# MERGE  = joining DataFrames using a common column (like SQL JOIN)

# -----------------------------------------------
# KEY TAKEAWAYS
# -----------------------------------------------
# 1. pd.concat() is used to combine DataFrames
# 2. axis=0 → add rows (default)
# 3. axis=1 → add columns
# 4. ignore_index=True resets the index
# 5. Missing columns will result in NaN values
# 6. Use CONCAT for stacking, MERGE for matching columns