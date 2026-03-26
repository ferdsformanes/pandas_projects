# -----------------------------------------------
# Handling Missing Data in Pandas
# -----------------------------------------------

import pandas as pd

# -----------------------------------------------
# Step 1: Load Excel File
# -----------------------------------------------
# Read the demo file with missing values
df = pd.read_excel("demo_missing_methods.xlsx")

print(df.head())


# -----------------------------------------------
# Step 2: Detect Missing Values
# -----------------------------------------------

# Show True/False for missing values
print(df.isna())

# Count missing values per column
print(df.isna().sum())


# -----------------------------------------------
# Step 3: Detect Non-Missing Values
# -----------------------------------------------

# Opposite of isna()
print(df.notna())


# -----------------------------------------------
# Step 4: Handle Empty Strings (Important!)
# -----------------------------------------------

# Convert empty strings "" to real NaN values
df = df.replace("", pd.NA)

# Re-check missing values
print(df.isna().sum())


# -----------------------------------------------
# Step 5: Drop Missing Data
# -----------------------------------------------

# Drop rows with ANY missing value
df_drop_any = df.dropna()
print(df_drop_any)

# Drop rows only if ALL values are missing
df_drop_all = df.dropna(how='all')
print(df_drop_all)


# -----------------------------------------------
# Step 6: Fill Missing Values
# -----------------------------------------------

df_filled = df.fillna({
    'city': 'Unknown',
    'street': 'No Street',
    'company_name': 'No Company'
})

print(df_filled)


# -----------------------------------------------
# Step 7: Final Output
# -----------------------------------------------

df_filled.to_excel("cleaned_missing_data.xlsx", index=False)


# -----------------------------------------------
# KEY TAKEAWAYS:
# -----------------------------------------------
# 1. isna() → detect missing values
# 2. notna() → detect valid values
# 3. replace("", pd.NA) → handle empty strings
# 4. dropna() → remove missing data
# 5. fillna() → replace missing values