# Pandas DataFrame vs Series

import pandas as pd

# Step 1: Read Excel file → creates a DataFrame (table)
df = pd.read_excel("sdwan_devices.xlsx")
print(df.head())  
print(type(df))

# DataFrame:
# - 2D (rows + columns)
# - Example: full SD-WAN device table

# --------------------------------------------------

# Step 2: Select one column → creates a Series
hostnames = df["host-name"]
print(hostnames)  
print(type(hostnames))

# Series:
# - 1D (one column only)
# - Example: just the host-name column

# Key idea:
# A DataFrame = multiple columns (table)
# A Series = single column