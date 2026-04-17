# -----------------------------------------------
# Grouping Data in Pandas (groupby)
# -----------------------------------------------

# -----------------------------------------------
# WHAT IS groupby()?
# -----------------------------------------------
# groupby() is a Pandas method used to split data into groups
# based on a column, then apply calculations like sum, mean, or count.

# -----------------------------------------------
# Import pandas library
# -----------------------------------------------
import pandas as pd

# Make float output cleaner (apply globally)
pd.options.display.float_format = '{:.0f}'.format

# -----------------------------------------------
# CREATE SAMPLE DATAFRAME
# -----------------------------------------------
data = {
    "device_id": [1, 2, 3, 4, 5],
    "device_name": ["Router", "Switch", "Router", "Firewall", "Switch"],
    "site": ["SiteA", "SiteA", "SiteB", "SiteB", "SiteA"],
    "vendor": ["Cisco", "Cisco", "Juniper", "Palo Alto", "Cisco"],
    "cost": [700, 1000, 800, 500, 1200]
}

df = pd.DataFrame(data)
print(df)

# -----------------------------------------------
# BASIC GROUPBY (Single Column)
# -----------------------------------------------

grouped = df.groupby("device_name")["cost"].mean()
print(grouped)

# -----------------------------------------------
# GROUPBY WITH MULTIPLE AGGREGATIONS
# -----------------------------------------------

grouped = df.groupby("device_name")["cost"].agg(["count", "sum", "mean"])
print(grouped)

# -----------------------------------------------
# GROUPBY MULTIPLE COLUMNS
# -----------------------------------------------

grouped = df.groupby(["device_name", "site"])["cost"].sum()
print(grouped)

# -----------------------------------------------
# RESET INDEX (COMMON PRACTICE)
# -----------------------------------------------

# Convert result into a clean DataFrame (better for reading, reporting, and exporting)
grouped = df.groupby("device_name")["cost"].mean().reset_index()
print(grouped)

# -----------------------------------------------
# SORT GROUPED DATA
# -----------------------------------------------

grouped = df.groupby("device_name")["cost"].mean().sort_values(ascending=False).reset_index()
print(grouped)

# -----------------------------------------------
# REAL-WORLD INSIGHT EXAMPLES
# -----------------------------------------------

# Total cost per site (budget tracking)
site_cost = df.groupby("site")["cost"].sum().reset_index()

# Average vendor cost (compare vendors)
vendor_cost = df.groupby("vendor")["cost"].mean().reset_index()

# -----------------------------------------------
# KEY TAKEAWAYS
# -----------------------------------------------
# 1. groupby() method splits data into groups based on a column
# 2. Then you can apply aggregate functions like sum(), mean(), count()
# 3. agg() method allows multiple calculations at once
# 4. You can group by multiple columns
# 5. reset_index() is used to keep the result clean and tabular.
