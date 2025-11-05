import pandas as pd

# Load the CSV file
df = pd.read_csv('sample_ip_addresses.csv')

# Remove duplicate rows
df_cleaned = df.drop_duplicates()

# Save the cleaned file
df_cleaned.to_csv('sample_ip_addresses_cleaned.csv', index=False)

print("Duplicates removed. Cleaned file saved as 'sample_ip_addresses_cleaned.csv'.")
