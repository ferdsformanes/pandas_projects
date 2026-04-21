# -----------------------------------------------
# Visualizing Data in Pandas (plot)
# -----------------------------------------------

# -----------------------------------------------
# WHAT IS plot()?
# -----------------------------------------------
# plot() is a Pandas method used to visualize data quickly.
# It allows you to create charts like line, bar, and pie
# directly from a DataFrame or Series.

# -----------------------------------------------
# Import libraries
# -----------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt

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
# BASIC PLOT (LINE CHART: DEFAULT PLOT TYPE IN PANDAS)
# -----------------------------------------------

# Plot cost over index
df["cost"].plot()
plt.title("Device Cost Trend")
plt.show()

# -----------------------------------------------
# BAR CHART (VERY COMMON)
# -----------------------------------------------

# Total cost per device
device_cost = df.groupby("device_name")["cost"].sum()

device_cost.plot(kind="bar")
plt.title("Total Cost per Device Type")
plt.xlabel("Device Type")
plt.ylabel("Total Cost")
plt.show()

# -----------------------------------------------
# BAR CHART (PER SITE)
# -----------------------------------------------

# Total cost per site
site_cost = df.groupby("site")["cost"].sum()

site_cost.plot(kind="bar")
plt.title("Total Cost per Site")
plt.xlabel("Site")
plt.ylabel("Total Cost")
plt.show()

# -----------------------------------------------
# PIE CHART (DISTRIBUTION)
# -----------------------------------------------

# Cost distribution per vendor
vendor_cost = df.groupby("vendor")["cost"].sum()

vendor_cost.plot(kind="pie", autopct='%1.1f%%')
plt.title("Cost Distribution per Vendor")
plt.ylabel("")  # cleaner look
plt.show()

# -----------------------------------------------
# MULTI-COLUMN GROUP + PLOT
# -----------------------------------------------

# Cost per device per site
multi = df.groupby(["device_name", "site"])["cost"].sum().unstack()

multi.plot(kind="bar")
plt.title("Cost per Device per Site")
plt.xlabel("Device Type")
plt.ylabel("Cost")
plt.show()

# -----------------------------------------------
# KEY TAKEAWAYS
# -----------------------------------------------
# 1. plot() lets you visualize data directly in Pandas
# 2. Use kind="bar", "line", "pie" for different charts
# 3. groupby() + plot() is powerful for analysis
# 4. plt.show() displays the chart
