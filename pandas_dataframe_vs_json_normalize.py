# -----------------------------------------------
# Pandas DataFrame vs json_normalize()
# -----------------------------------------------

# Import Libraries
import requests
import pandas as pd

# Get JSON Data from API
response = requests.get("https://jsonplaceholder.typicode.com/users")
data = response.json()

# -----------------------------------------------
# Using DataFrame() (keeps nested structure)
# -----------------------------------------------

df_raw = pd.DataFrame(data)
print(df_raw.columns)

print(df_raw['address'][0])      # Works, but uses chained indexing
print(df_raw.loc[0, 'address'])  # Recommended: uses .loc[row, column] (clear and safe)

df_raw.to_excel("raw_data.xlsx", index=False)

# -----------------------------------------------
# Using json_normalize() (flattens nested JSON into columns)
# -----------------------------------------------

df_flat = pd.json_normalize(data, sep="_")  # sep="_" replaces nested keys (address.city -> address_city)
print(df_flat.columns)
df_flat.to_excel("flat_data.xlsx", index=False)

# -----------------------------------------------
# Selecting Columns
# -----------------------------------------------

df_selected = df_flat[['name', 'email', 'address_street', 'address_city', 'company_name']]

# -----------------------------------------------
# Output
# -----------------------------------------------

print(df_selected.head())
print(df_selected.head(1).T)

# -----------------------------------------------
# KEY TAKEAWAYS:
# -----------------------------------------------
# 1. DataFrame() = keeps JSON structure (nested data stays as dict)
# 2. json_normalize() = flattens JSON (nested fields become columns)
# 3. Use json_normalize() for easier access to nested data from APIs