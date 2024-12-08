This project contains scripts to clean and analyze weather and solar radiation data from Benin Malanville. The scripts handle data preprocessing, outlier detection, and summary statistics calculation, and provide detailed reports on the number of records before and after cleaning.

Setup and Installation
Prerequisites
Make sure you have Python and pip installed. Then, install the required libraries using the provided requirements.txt file.

Installation
Clone the repository:

git clone <repository_url>
Navigate to the project directory:

cd <project_directory>
Install the required packages:

pip install -r requirements.txt


Running the Scripts
Data Cleaning Script
The data_cleaning.py script performs the following steps:

Loads the CSV data and drops the Timestamp column.

Detects and handles outliers using the Interquartile Range (IQR) method.

Fills missing values with the median of the columns.

Removes rows with negative values in key solar radiation parameters (GHI, DNI, DHI).

Saves the cleaned data to a new CSV file.

Compares the number of records before and after cleaning.

Execution:

Run the script using Python:

python3 data_cleaning.py

Summary Statistics Script
The summary_statistics.py script performs the following steps:

Loads the CSV data and drops the Timestamp column.

Calculates summary statistics including mean, median, standard deviation, and other measures.

Saves the summary statistics to a new CSV file.

Execution:

Run the script using Python:
python3 summary_statistics.py
