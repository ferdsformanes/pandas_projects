# -----------------------------------------------
# Handling Missing Data in Pandas
# -----------------------------------------------

import pandas as pd

# -----------------------------------------------
# Load Excel File
# -----------------------------------------------

df = pd.read_excel("sdwan_devices.xlsx")

print(df.head())


# -----------------------------------------------
# Detect Missing Data
# -----------------------------------------------

print(df.isna())          # True/False mask
print(df.isna().sum())    # Count per column
print(df.notna())         # Opposite of isna()


# -----------------------------------------------
# Hidden Missing Values (Empty Strings)
# -----------------------------------------------

# NOTE:
# Empty strings ("") are NOT considered missing by Pandas
# We will handle this in a separate example

print(df.isna().sum())    # Still the same


# -----------------------------------------------
# Remove Missing Data
# -----------------------------------------------

df_drop_any = df.dropna()             # Drop rows with ANY missing value
df_drop_all = df.dropna(how='all')    # Drop rows where ALL values are missing

print(df_drop_any)
print(df_drop_all)


# -----------------------------------------------
# Fill Missing Data
# -----------------------------------------------

df_filled = df.fillna({
    'reachability': 'unknown',
    'system-ip': '1.1.1.1',
})

print(df_filled)


# -----------------------------------------------
# Save Cleaned Data
# -----------------------------------------------

df_filled.to_excel("cleaned_missing_data_sdwan_devices.xlsx", index=False)


# -----------------------------------------------
# KEY TAKEAWAYS
# -----------------------------------------------
# isna()   → detect missing values
# notna()  → detect valid values
# dropna() → remove missing data
# fillna() → replace missing values
