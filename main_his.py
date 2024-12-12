import kaggle
import os
import pandas as pd

# Set Kaggle API credentials directory
os.environ['KAGGLE_CONFIG_DIR'] = r'C:/Users/sunny/.kaggle'  # Update this path to your Kaggle configuration directory

# Specify the dataset identifier
dataset ='muhammadehsan02/126-years-of-historical-olympic-dataset'

# Set the download path
download_path = 'C:/POWER BI AND SQL PROJECT/Historical' # Change this to your preferred download directory

# Remove existing files in the folder to prevent duplicates or outdated files
for file in os.listdir(download_path):
    file_path = os.path.join(download_path, file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)  # Delete the file
            print(f"Deleted {file_path}")
    except Exception as e:
        print(f"Error deleting {file_path}: {e}")

# Download the dataset using the Kaggle API and unzip the files
kaggle.api.dataset_download_files(dataset, path=download_path, unzip=True)

# List of CSV files to be imported
csv_files = [
'Olympic_Athlete_Biography.csv'
'Olympic_Athlete_Event_Details.csv'
'Olympic_Country_Profiles.csv'
'Olympic_Event_Results.csv'
'Olympic_Games_Summary.csv'
'Olympic_Medal_Tally_History.csv'
]

# Initialize a dictionary to hold DataFrames
dataframes = {}

# Iterate through each CSV file and load it into a DataFrame
for file in csv_files:
    # Construct the full path to the CSV file
    file_path = os.path.join(download_path, file)
    
    # Load the CSV file into a Pandas DataFrame
    df = pd.read_csv(file_path)
    
    # Add the DataFrame to the dictionary using the file name as the key
    table_name = file.split('.')[0]  # Remove the .csv extension
    dataframes[table_name] = df