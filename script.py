# Import necessary libraries
from datetime import datetime
import pandas as pd
import winshell
import os
import time

# Define paths and file locations
DesktopPath = winshell.desktop()
CurrentFolder = DesktopPath + '\\ForexProgram'
BaseDataFilePath = CurrentFolder + '\\BaseDataDict.txt'
BaseDataDict = pd.read_csv(BaseDataFilePath, header=None, index_col=0, squeeze=True).to_dict()

# Extract settings from the configuration file
MetaTimeZoneDifferenceInHours = int(BaseDataDict['MetaTimeZoneDifferenceInHours'])  # Timezone difference in hours
MetaTraderIndicatorFilePath = BaseDataDict['MetaTraderIndicatorFilePath']  # Path to MetaTrader indicator file
AllDetectedLevelsFilePath = BaseDataDict['AllDetectedLevelsFilePath']  # Path to detected levels file

# Create an empty DataFrame to store MetaTrader indicator data
CurrentMetaLevels2 = pd.DataFrame()

# Read MetaTrader indicator data from a CSV file
CurrentMetaLevels = pd.read_csv(MetaTraderIndicatorFilePath)

# Convert the 'Time1' column to datetime objects
CurrentMetaLevels.loc[:, 'Time1'] = pd.to_datetime(CurrentMetaLevels.loc[:, 'Time1'], format="%Y-%m-%d %H:%M:%S.%f")

# Create an additional 'Time' column as timestamps
CurrentMetaLevels['Time'] = CurrentMetaLevels['Time1'].apply(lambda x: x.timestamp())

# Initialize an empty string for building MetaTrader script
Text = ""

# Iterate through rows in the MetaTrader indicator data
for i in range(CurrentMetaLevels.shape[0]):
    # Build a MetaTrader script command for drawing a box
    Text += ("box.new(" +
             str(int(CurrentMetaLevels.loc[i, "Time"]) * 1000 - 2 * 60 * 60 * 1000) + "," +
             str(CurrentMetaLevels.loc[i, "price1"]) + "," +
             str(int(CurrentMetaLevels.loc[i, "Time"]) * 1000 - 2 * 60 * 60 * 1000 + 60000) + "," +
             str(CurrentMetaLevels.loc[i, "price2"]) + "," +
             "color.purple, 1, line.style_solid, extend.right, xloc.bar_time, color.new(color.purple, 90)," +
             "input.string(\"" + CurrentMetaLevels.loc[i, "Text1"] + "\"))" + "\n")

# The 'Text' string now contains the MetaTrader script commands for drawing boxes

# Note: The code is primarily focused on extracting data from CSV files and creating MetaTrader script commands.
# The extracted data is used to draw boxes on a MetaTrader chart.
