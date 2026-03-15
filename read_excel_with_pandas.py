# How to Read and Explore an Excel File Using Pandas

# Step 1 — Import pandas
import pandas as pd

# Step 2 — Read the Excel file into a DataFrame
df = pd.read_excel("sdwan_devices.xlsx")

# Step 3 — View the first 5 rows
df.head()

# Step 4 — Check the column names
df.columns

# Step 5 — Check the structure of the DataFrame
df.info()

# Step 6 — Check the data types of each column
df.dtypes

# Step 7 — See the shape of the DataFrame (rows, columns)
df.shape

# Step 8 — Check for missing values
df.isna()

# Step 9 — Count unique values in a column
df["device-type"].value_counts()

# Step 10 — Select specific columns
df = df[["host-name", "device-type", "system-ip", "reachability"]]

# Step 11 — View the filtered data
df.head()