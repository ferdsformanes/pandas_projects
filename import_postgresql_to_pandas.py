# -----------------------------------------------
# How to Import Data from PostgreSQL into Pandas
# -----------------------------------------------

import pandas as pd
from sqlalchemy import create_engine

# -----------------------------------------------
# Connect to PostgreSQL using SQLAlchemy
# -----------------------------------------------

# Format: dialect+connector://username:password@host:port/database
engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5433/testdb")

# -----------------------------------------------
# Read Data from PostgreSQL into DataFrame
# -----------------------------------------------

# Read all columns from the table
df = pd.read_sql("SELECT * FROM sdwan_devices", con=engine)

print(df)


# -----------------------------------------------
# Export DataFrame to Excel
# -----------------------------------------------

# Save DataFrame to an Excel file
df.to_excel("sdwan_devices.xlsx", index=False)

print("Data exported to sdwan_devices.xlsx successfully!")


# -----------------------------------------------
# KEY TAKEAWAYS
# -----------------------------------------------
# read_sql() → read data from database into DataFrame
# SELECT *   → select all columns
# engine     → database connection
# to_excel() → export DataFrame to Excel file