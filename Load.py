# Import necessary libraries
import pandas as pd
import os

# Define the path to the downloaded CSV files
download_path = r'C:\POWER BI AND SQL PROJECT\source'

# Load the data into DataFrames
athletes = pd.read_csv(os.path.join(download_path, 'athletes.csv'))
events = pd.read_csv(os.path.join(download_path, 'events.csv'))
medallists = pd.read_csv(os.path.join(download_path, 'medallists.csv'))
medals = pd.read_csv(os.path.join(download_path, 'medals.csv'))
medals_total = pd.read_csv(os.path.join(download_path, 'medals_total.csv'))
schedules = pd.read_csv(os.path.join(download_path, 'schedules.csv'))
schedules_preliminary = pd.read_csv(os.path.join(download_path, 'schedules_preliminary.csv'))
teams = pd.read_csv(os.path.join(download_path, 'teams.csv'))
torch_route = pd.read_csv(os.path.join(download_path, 'torch_route.csv'))
venues = pd.read_csv(os.path.join(download_path, 'venues.csv'))
