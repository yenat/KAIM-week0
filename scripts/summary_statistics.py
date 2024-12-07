import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('../data/benin-malanville.csv')

# Drop the Timestamp column 
df.drop(columns=['Timestamp'], inplace=True)

# Calculate summary statistics
summary_stats = df.describe().transpose()

# Additional calculations (e.g., median)
summary_stats['median'] = df.median()

# Select only the required columns
statistical_measures = summary_stats[['mean', '50%', 'std', 'min', '25%', '75%', 'max', 'median']]

# Rename '50%' to 'median'
statistical_measures.rename(columns={'50%': 'median'}, inplace=True)

# Save only the column names and their statistical measures to a new CSV file
statistical_measures.to_csv('benin_summary_statistics.csv', index_label='Column')

print("Benin summary statistics saved to benin_summary_statistics.csv")
