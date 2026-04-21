# -----------------------------------------------
# TIME SERIES IN PANDAS
# -----------------------------------------------

# -----------------------------------------------
# WHAT IS A TIME SERIES?
# -----------------------------------------------
# A time series is data indexed by time (dates or timestamps).
# Examples:
# - Device count per day
# - License usage over time
# - CPU utilization per minute
#
# In Pandas, Time Series = Date/Time + Index + Operations

# -----------------------------------------------
# Import libraries
# -----------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------------------
# CREATE SAMPLE TIME SERIES DATA
# -----------------------------------------------

data = {
    "date": [
        "2026-04-01",
        "2026-04-02",
        "2026-04-03",
        "2026-04-04",
        "2026-04-05"
    ],
    "device_count": [120, 125, 123, 130, 135],
    "license_used": [300, 305, 302, 310, 315]
}

df = pd.DataFrame(data)

# -----------------------------------------------
# CONVERT DATE COLUMN TO datetime
# -----------------------------------------------
# Pandas needs real datetime objects for time operations

df["date"] = pd.to_datetime(df["date"])

print(df.dtypes)

# -----------------------------------------------
# SET DATE AS INDEX (VERY IMPORTANT)
# -----------------------------------------------
# Time series operations work best with datetime index

df = df.set_index("date")
print(df)

# -----------------------------------------------
# BASIC TIME SERIES PLOT
# -----------------------------------------------

df["device_count"].plot()
plt.title("Device Count Over Time")
plt.xlabel("Date")
plt.ylabel("Number of Devices")
plt.show()

# -----------------------------------------------
# MULTIPLE COLUMNS TIME SERIES PLOT
# -----------------------------------------------

df.plot()
plt.title("Devices and License Usage Over Time")
plt.xlabel("Date")
plt.ylabel("Count")
plt.show()

# -----------------------------------------------
# DATE-BASED SELECTION (SLICING)
# -----------------------------------------------
# Select data for a specific date or range

print(df.loc["2026-04-02"])
print(df.loc["2026-04-02":"2026-04-04"])

# -----------------------------------------------
# RESAMPLING (VERY COMMON)
# -----------------------------------------------
# Resampling = change time frequency
# Example: daily → weekly / monthly

weekly = df.resample("W").mean()
print(weekly)

weekly.plot()
plt.title("Weekly Average Metrics")
plt.show()

# -----------------------------------------------
# ROLLING WINDOW (MOVING AVERAGE)
# -----------------------------------------------
# Used for smoothing and trend detection

df["device_count_ma"] = df["device_count"].rolling(window=3).mean()

df[["device_count", "device_count_ma"]].plot()
plt.title("Device Count with Moving Average")
plt.show()

# -----------------------------------------------
# SHIFTING DATA (COMPARISON OVER TIME)
# -----------------------------------------------
# Used to compare with previous values

df["previous_day"] = df["device_count"].shift(1)
df["daily_change"] = df["device_count"] - df["previous_day"]

print(df)

# -----------------------------------------------
# KEY TAKEAWAYS
# -----------------------------------------------
# 1. Always convert date columns to datetime
# 2. Set date as index for time series operations
# 3. resample() is used to change time frequency
# 4. rolling() helps smooth noisy data
# 5. shift() helps compare values across time
