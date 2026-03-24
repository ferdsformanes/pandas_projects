# -----------------------------------------------
# Pandas DataFrame vs json_normalize()
# -----------------------------------------------

# Step 1: Import Libraries
import requests
import pandas as pd

# Step 2: Get JSON Data from API
response = requests.get("https://jsonplaceholder.typicode.com/users")
data = response.json()

# Step 3: Convert JSON using DataFrame()
# This keeps nested JSON as dictionaries
df_raw = pd.DataFrame(data)
print(df_raw.columns)

print(df_raw['address'][0])
df_raw.to_excel("raw_data.xlsx", index=False)  

# Step 4: Convert JSON using json_normalize()
# This flattens nested JSON into columns

df_flat = pd.json_normalize(data, sep="_")
print(df_flat.columns)
df_flat.to_excel("flat_data.xlsx", index=False) 

# Step 5: Select Nested Fields Easily
# Notice we can directly access nested fields using dot notation

df_selected = df_flat[['name', 'email', 'address_city', 'company_name']]

# Step 6: Final Output
print(df_selected.head())


# -----------------------------------------------
# KEY TAKEAWAYS:
# -----------------------------------------------
# 1. DataFrame() = keeps JSON structure (nested data stays as dict)
# 2. json_normalize() = flattens JSON (nested fields become columns)
# 3. json_normalize() is very useful when working with APIs