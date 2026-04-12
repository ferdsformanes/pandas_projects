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
# dtypes = shows what kind of data each column holds (e.g., number, text, True/False)
print(df.dtypes)

# -----------------------------------------------
# Common Pandas Data Types
# -----------------------------------------------
# int64     → integers
# float64   → floating-point numbers
# object    → strings (text)  # generic Python object (strings are stored as objects)
# bool      → True/False

# -----------------------------------------------
# Convert Data Type (astype)
# -----------------------------------------------
# Convert price from int to float
df["price"] = df["price"].astype(float)

print(df.dtypes)

# -----------------------------------------------
# Convert Integer to String
# -----------------------------------------------
# Sometimes numbers are used as labels (e.g., IDs)
df["device_id"] = df["device_id"].astype(str)

print(df.dtypes)

# -----------------------------------------------
# Convert String to Numeric
# -----------------------------------------------
df2 = pd.DataFrame({
    "device_id": ["1", "2", "3"]  # stored as string
})

print(df2.dtypes)

df2["device_id"] = df2["device_id"].astype(int)

print(df2.dtypes)

# -----------------------------------------------
# Handle Errors (invalid conversion)
# -----------------------------------------------
df3 = pd.DataFrame({
    "price": ["100", "200", "invalid"]
})

# errors="coerce" → invalid values become NaN instead of crashing
df3["price"] = pd.to_numeric(df3["price"], errors="coerce")

print(df3)

# -----------------------------------------------
# Timestamp (VERY common in networking logs)
# -----------------------------------------------
df4 = pd.DataFrame({
    "log_time": ["2026-04-10 10:00:00", "2026-04-10 10:05:00", "2026-04-10 10:10:00"]
})

print(df4.dtypes)

# Convert string dates into real datetime objects
# Enables filtering, sorting, and time-based analysis
df4["log_time"] = pd.to_datetime(df4["log_time"])

print(df4.dtypes)

# -----------------------------------------------
# KEY TAKEAWAYS
# -----------------------------------------------
# 1. dtype tells you the type of data in each column
# 2. Use df.dtypes to check column types
# 3. Common types: int, float, object, bool, datetime64
# 4. Use astype() to convert data types
# 5. Use pd.to_numeric() for safer numeric conversions
# 6. Use pd.to_datetime() for timestamps (very important in logs and networking data)
# 7. errors="coerce" turns invalid values into NaN instead of crashing

# Read https://pbpython.com/pandas_dtypes.html before making a video on this topic!