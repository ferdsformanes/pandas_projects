# -------------------------------
# Pandas iloc vs loc Explained (Excel-Based Tutorial)
# -------------------------------

# loc (label location) - label-based, meaning you select rows and columns by index labels and column names.
# iloc (integer location) - integer position-based, meaning you select rows and columns by their integer positions (row 0 = first row, column 0 = first column).

import pandas as pd

# -------------------------------
# Step 1: Load Excel File
# -------------------------------
df = pd.read_excel(r"C:\Users\user\Desktop\ftc\Topics\Python\Projects\sdwan\devices.xlsx")

# Strip column names
df.columns = df.columns.str.strip()

# =====================================================
# PART 1: iloc ("integer location") - Integer position-based
# =====================================================
# Syntax:
# df.iloc[row_index, column_index] → single value
# df.iloc[row_index] → entire row
# df.iloc[:, column_index] → entire column

# Examples:
val = df.iloc[0, 0]           # first row, first column
first_row = df.iloc[0]        # first row
first_col = df.iloc[:, 0]     # first column
first_two_rows = df.iloc[0:2] # first two rows (exclusive)

# =====================================================
# PART 2: loc ("label location") - Label-based
# =====================================================
# Syntax:
# df.loc[row_label, column_label] → single value
# df.loc[row_label] → entire row
# df.loc[:, column_label] → entire column

# Examples:
hostname_val = df.loc[0, "hostname"]                # row 0, column 'hostname'
hostname_col = df.loc[:, "hostname"]                # entire 'hostname' column
host_dev_cols = df.loc[:, ["hostname", "device_type"]]  # multiple columns
cisco_devices = df.loc[df["device_type"] == "cisco_ios_telnet"]  # conditional filter
rows_0_1 = df.loc[0:1]                              # rows 0 to 1 (inclusive)

