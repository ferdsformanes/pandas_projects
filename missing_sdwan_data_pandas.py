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
# Pandas does NOT consider empty cells that contain "" (empty string)
# or only spaces ("   ") as missing values by default.
# We replace them with pd.NA to mark them as true missing values.
df = df.replace(r'^\s*$', pd.NA, regex=True)

# Now these "hidden" missing values will be detected
print(df.isna().sum())

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
    'deviceId': 'unknown',
    'system-ip': 'unknown',
    'reachability': 'unknown',

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
