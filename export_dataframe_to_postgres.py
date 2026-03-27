# -----------------------------------------------
# Exporting a Pandas DataFrame to PostgreSQL
# -----------------------------------------------

import pandas as pd
from sqlalchemy import create_engine

# -----------------------------------------------
# Read the example data into a DataFrame
# -----------------------------------------------
df = pd.read_excel('sdwan_devices.xlsx') 
print(df)

# -----------------------------------------------
# Connect to PostgreSQL using SQLAlchemy
# -----------------------------------------------

# Format: postgresql+psycopg2://username:password@host:port/database
engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5433/testdb")

# -----------------------------------------------
# Export DataFrame to PostgreSQL
# -----------------------------------------------

# df.to_sql parameters:
# - name: table name
# - con: SQLAlchemy engine
# - if_exists: 'fail', 'replace', 'append'
# - index: whether to write the DataFrame index as a column
df.to_sql(
    name='sdwan_devices', 
    con=engine, 
    if_exists='replace', 
    index=False
)

print("Data exported successfully to PostgreSQL!")