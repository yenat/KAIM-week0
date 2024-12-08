import pandas as pd
import numpy as np

# Load the CSV file into a DataFrame
df = pd.read_csv('../data/benin-malanville.csv')

# Drop the Timestamp column
df.drop(columns=['Timestamp'])

# Columns to check for negative values
columns_to_check = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust']

# Define function to detect outliers using IQR
def detect_outliers(series):
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return ((series < lower_bound) | (series > upper_bound))

# Apply outlier detection and handle outliers
for column in columns_to_check:
    outliers = detect_outliers(df[column])
    df.loc[outliers, column] = np.nan  # Set outliers to NaN

# Fill missing values (e.g., using median)
for column in columns_to_check:
    df[column].fillna(df[column].median())

# Handle incorrect entries (negative values in GHI, DNI, DHI) by removing those rows
incorrect_entries = (df['GHI'] < 0) | (df['DNI'] < 0) | (df['DHI'] < 0)
df = df[~incorrect_entries]

# Save the cleaned data to a new CSV file
df.to_csv('cleaned_data.csv', index=False)

print("Cleaned data saved to cleaned_data.csv")

# Load the CSV files into DataFrames
df1 = pd.read_csv('../data/benin-malanville.csv')
df2 = pd.read_csv('../data/cleaned_data.csv')

# Get the number of records in each DataFrame
num_records_file1 = len(df1)
num_records_file2 = len(df2)

# Print the number of records and compare
print(f"Number of records from the original file: {num_records_file1} " f"has reduced to {num_records_file2} after cleaning.")

