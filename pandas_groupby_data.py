# -----------------------------------------------
# Grouping Data in Pandas (groupby)
# -----------------------------------------------

# -----------------------------------------------
# WHY GROUP DATA?
# -----------------------------------------------
# 1. Summarize data easily
# 2. Find totals, averages, counts
# 3. Analyze patterns by category
# 4. Useful for reports and dashboards

# -----------------------------------------------
# Import pandas library
# -----------------------------------------------
import pandas as pd

# -----------------------------------------------
# CREATE SAMPLE DATAFRAME
# -----------------------------------------------
data = {
    "device_id": [1, 2, 3, 4, 5],
    "device_name": ["Router", "Switch", "Router", "Firewall", "Switch"],
    "location": ["SiteA", "SiteA", "SiteB", "SiteB", "SiteA"],
    "price": [700, 1000, 800, 500, 1200]
}

df = pd.DataFrame(data)
print(df)

# -----------------------------------------------
# BASIC GROUPBY (Single Column)
# -----------------------------------------------

# Group by device_name and get average price
grouped = df.groupby("device_name")["price"].mean()
print(grouped)

# -----------------------------------------------
# GROUPBY WITH MULTIPLE AGGREGATIONS
# -----------------------------------------------

# Get count, sum, and average price per device
grouped = df.groupby("device_name")["price"].agg(["count", "sum", "mean"])
print(grouped)

# -----------------------------------------------
# GROUPBY MULTIPLE COLUMNS
# -----------------------------------------------

# Group by device_name and location
grouped = df.groupby(["device_name", "location"])["price"].sum()
print(grouped)

# -----------------------------------------------
# RESET INDEX (COMMON PRACTICE)
# -----------------------------------------------

grouped = df.groupby("device_name")["price"].mean().reset_index()
print(grouped)

# -----------------------------------------------
# SORT GROUPED DATA
# -----------------------------------------------

grouped = df.groupby("device_name")["price"].mean().sort_values(ascending=False)
print(grouped)

# -----------------------------------------------
# KEY TAKEAWAYS
# -----------------------------------------------
# 1. groupby() is used to group data by category
# 2. Use aggregation functions like sum(), mean(), count()
# 3. agg() allows multiple calculations at once
# 4. You can group by multiple columns
# 5. reset_index() makes output cleaner