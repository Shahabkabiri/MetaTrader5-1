# MetaTrader Indicator Data Processor

This Python script is designed to process MetaTrader indicator data and generate MetaTrader script commands for drawing boxes on a MetaTrader chart. It reads configuration settings and indicator data from CSV files, converts timestamps, and creates the necessary script commands.

## Prerequisites

- Python
- pandas
- winshell (for Windows desktop path)

## Usage

1. Clone this repository.
2. Ensure that you have the necessary CSV files and configuration data in the specified locations:
   - `BaseDataDict.txt`: Contains configuration settings.
   - `MetaTraderIndicatorFilePath`: Path to the MetaTrader indicator CSV file.
   - `AllDetectedLevelsFilePath`: Path to the detected levels file.
3. Modify the script's variables if needed:
   - Update the file paths in `BaseDataFilePath`, `MetaTraderIndicatorFilePath`, and `AllDetectedLevelsFilePath` to point to your own data files.
4. Run the script.

## Description

This script performs the following tasks:

- Reads configuration settings from `BaseDataDict.txt`, including timezone differences.
- Reads MetaTrader indicator data from a CSV file specified in `MetaTraderIndicatorFilePath`.
- Converts timestamp data to datetime objects for processing.
- Generates MetaTrader script commands for drawing boxes on a MetaTrader chart based on the indicator data.
- The resulting `Text` string contains the script commands.

## Customization

You can customize the script by modifying the generated MetaTrader script commands. The script currently creates commands for drawing boxes, but you can adapt it for other charting elements or indicators.

## License

This project is licensed under the [MIT License](LICENSE).
