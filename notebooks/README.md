Data Analysis and Visualization
This project contains a comprehensive analysis of weather and solar radiation data, utilizing various data preprocessing, visualization, and statistical techniques. The analysis is conducted in a Jupyter Notebook, and this README.md will guide you through setting up the environment and understanding the analyses performed.

Setup and Installation
Prerequisites
Make sure you have Python and pip installed. Then, install the required libraries using the provided requirements.txt file.

Installation
Clone the repository:

bash
git clone <repository_url>
Navigate to the project directory:

bash
cd <project_directory>
Install the required packages:

bash
pip install -r requirements.txt
Running the Analysis
Open the Jupyter Notebook (data_analysis.ipynb) in VSCode or JupyterLab and execute the cells sequentially.

Step-by-Step Analysis
Data Loading and Setup:

Import necessary libraries.

Load the CSV data file.

Convert the Timestamp column to datetime and set it as the index.

Data Quality Check:

Identify and handle missing values and outliers.

Remove rows with negative values in key solar radiation parameters (GHI, DNI, DHI).

Summary Statistics:

Calculate and save mean, median, standard deviation, and other statistical measures for numeric columns.

Time Series Analysis:

Plot GHI, DNI, DHI, and Tamb over time to observe patterns by month and trends throughout the day.

Evaluate the impact of cleaning on sensor readings (ModA, ModB) over time.

Correlation Analysis:

Create correlation matrices and pair plots to visualize relationships between solar radiation components (GHI, DNI, DHI), temperature measures (TModA, TModB), and wind conditions (WS, WSgust, WD).

Histograms:

Create histograms for variables like GHI, DNI, DHI, WS, and temperatures to visualize the frequency distribution of these variables.

Z-Score Analysis:

Calculate Z-scores to flag data points significantly different from the mean.

Visualize flagged data points using scatter plots.

Bubble Charts:

Create bubble charts to explore complex relationships between variables (e.g., GHI vs. Tamb vs. WS) with bubble size representing an additional variable (RH or BP).

Wind Analysis:

Use radial bar plots or wind roses to identify trends and significant wind events by showing the distribution of wind speed and direction.

Temperature Analysis:

Examine how relative humidity (RH) influences temperature readings and solar radiation using scatter plots.