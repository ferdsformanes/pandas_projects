# -----------------------------------------------
# Visualizing Data in Pandas (plot)
# -----------------------------------------------

# -----------------------------------------------
# WHAT IS plot()?
# -----------------------------------------------
# plot() is a Pandas method used to quickly visualize data.
# It uses matplotlib behind the scenes to create charts
# like line, bar, and pie directly from your data.

# -----------------------------------------------
# Import libraries
# -----------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt

# Note: In Jupyter Notebook, plots may display automatically.
# In scripts (VS Code, .py files), plt.show() is required.

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
# Note: X-axis uses the DataFrame index by default
df["cost"].plot()  # Creates the chart using pandas (internally uses matplotlib)
plt.title("Device Cost Trend")  # Adds title to the current active plot
plt.show()  # Displays the chart (matplotlib shows whatever was already created)

# -----------------------------------------------
# BAR CHART (VERY COMMON)
# -----------------------------------------------

# Total cost per device
device_cost = df.groupby("device_name")["cost"].sum()

device_cost.plot(kind="bar")  # Creates the bar chart using pandas (uses matplotlib internally)
plt.title("Total Cost per Device Type")  # Adds title to the current active plot
plt.xlabel("Device Type")  # Labels the x-axis of the current plot
plt.ylabel("Total Cost")  # Labels the y-axis of the current plot
plt.show()  # Displays the chart (matplotlib shows whatever was already created)

# -----------------------------------------------
# BAR CHART (PER SITE)
# -----------------------------------------------

# Total cost per site
site_cost = df.groupby("site")["cost"].sum()

site_cost.plot(kind="bar")  # Creates bar chart from grouped data
plt.title("Total Cost per Site")  # Adds title to the current active plot
plt.xlabel("Site")  # Labels the x-axis
plt.ylabel("Total Cost")  # Labels the y-axis
plt.show()  # Displays the chart

# -----------------------------------------------
# PIE CHART (DISTRIBUTION)
# -----------------------------------------------

# Cost distribution per vendor
vendor_cost = df.groupby("vendor")["cost"].sum()

vendor_cost.plot(kind="pie", autopct='%1.1f%%')  # Creates pie chart and shows percentage labels
plt.title("Cost Distribution per Vendor")  # Adds title
plt.ylabel("")  # Removes y-label for cleaner look
plt.show()  # Displays the chart

# -----------------------------------------------
# MULTI-COLUMN GROUP + PLOT
# -----------------------------------------------

# Cost per device per site
# unstack() moves "site" from rows into columns,
# making the data easier to visualize as grouped bars
multi = df.groupby(["device_name", "site"])["cost"].sum().unstack()

multi.plot(kind="bar")  # Creates grouped bar chart
plt.title("Cost per Device per Site")  # Adds title
plt.xlabel("Device Type")  # Labels the x-axis
plt.ylabel("Cost")  # Labels the y-axis
plt.show()  # Displays the chart

# -----------------------------------------------
# KEY TAKEAWAYS
# -----------------------------------------------
# 1. plot() lets you visualize data directly in Pandas
# 2. Use kind="bar", "line", "pie" for different charts
# 3. groupby() + plot() is powerful for analysis
# 4. plt.show() displays the chart
# 5. Pandas handles the data, matplotlib handles the visualization