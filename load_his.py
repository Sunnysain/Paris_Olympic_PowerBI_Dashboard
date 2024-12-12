# Import necessary libraries
import pandas as pd
import os

# Define the path to the downloaded CSV files
download_path = r'C:\POWER BI AND SQL PROJECT\Historical'

# Load the data into DataFrames
Historical = pd.read_csv(os.path.join(download_path, 'Olympic_Medal_Tally_History.csv'))