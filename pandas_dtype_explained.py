# -----------------------------------------------
# Pandas dtype Explained (Understand Data Types Easily)
# -----------------------------------------------

import pandas as pd

# -----------------------------------------------
# Create Sample DataFrame
# -----------------------------------------------
data = {
    "device_id": [1, 2, 3],
    "device_name": ["Router", "Switch", "Firewall"],
    "price": [1000, 500, 750],
    "is_active": [True, False, True]
}

df = pd.DataFrame(data)

print(df)

# -----------------------------------------------
# Check Data Types (dtypes)
# -----------------------------------------------
# Shows the data type of each column
print(df.dtypes)

# -----------------------------------------------
# Common Pandas Data Types
# -----------------------------------------------
# int64    → integers
# float64  → decimal numbers
# object   → strings (text)
# bool     → True/False

# -----------------------------------------------
# Convert Data Type (astype)
# -----------------------------------------------
# Convert price from int to float
df["price"] = df["price"].astype(float)

print(df.dtypes)

# -----------------------------------------------
# Convert String to Numeric
# -----------------------------------------------
df2 = pd.DataFrame({
    "device_id": ["1", "2", "3"]  # stored as string
})

print(df2.dtypes)

# Convert to integer
df2["device_id"] = df2["device_id"].astype(int)

print(df2.dtypes)

# -----------------------------------------------
# Handle Errors (invalid conversion)
# -----------------------------------------------
df3 = pd.DataFrame({
    "price": ["100", "200", "invalid"]
})

# Use to_numeric to handle errors
df3["price"] = pd.to_numeric(df3["price"], errors="coerce")

print(df3)

# -----------------------------------------------
# KEY TAKEAWAYS
# -----------------------------------------------
# 1. dtype tells you the type of data in each column
# 2. Use df.dtypes to check column types
# 3. Common types: int, float, object, bool
# 4. Use astype() to convert data types
# 5. Use pd.to_numeric() for safer conversions
# 6. errors="coerce" turns invalid values into NaN