# -----------------------------------------------
# Handling Missing Data in Pandas
# -----------------------------------------------

import pandas as pd

# Load Excel file
df = pd.read_excel("demo_missing_methods.xlsx")

print(df.head())


# -----------------------------------------------
# Detect Missing Data
# -----------------------------------------------

print(df.isna())          # True/False mask
print(df.isna().sum())   # Count per column

print(df.notna())        # Opposite of isna()


# -----------------------------------------------
# Handle Hidden Missing Values (Empty Strings)
# -----------------------------------------------

df = df.replace("", pd.NA)

print(df.isna().sum())   # Re-check after cleaning


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
    'city': 'Unknown',
    'street': 'No Street',
    'company_name': 'No Company'
})

print(df_filled)


# -----------------------------------------------
# Save Cleaned Data
# -----------------------------------------------

df_filled.to_excel("cleaned_missing_data.xlsx", index=False)


# -----------------------------------------------
# KEY TAKEAWAYS
# -----------------------------------------------
# isna()   → detect missing values
# notna()  → detect valid values
# replace("", pd.NA) → fix hidden missing data
# dropna() → remove missing data
# fillna() → replace missing values