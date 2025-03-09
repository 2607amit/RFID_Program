# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 12:30:46 2025

@author: Dell
"""

import os
import pandas as pd

# Define CSV storage location
csv_folder_path = os.path.join(os.path.expanduser("~"), "Documents", "amit", "csvFile")
csv_file_path = os.path.join(csv_folder_path, "test_cases.csv")

# Ensure the folder exists
os.makedirs(csv_folder_path, exist_ok=True)

# Define RFID file storage path
rfid_folder_path = "/Documents/amit/RFID_Files"

# Ensure RFID folder exists
os.makedirs(rfid_folder_path, exist_ok=True)

# Series and corresponding test case counts
series_test_cases = {
    1: 33, 2: 57, 3: 56, 4: 165, 5: 123, 6: 108, 7: 21, 8: 31, 9: 14, 10: 37, 
    11: 24, 12: 16, 13: 10, 14: 37, 15: 16, 16: 4, 17: 13, 18: 7, 19: 24, 20: 16,
    21: 20, 22: 35, 23: 24, 24: 67, 25: 47, 26: 41
}

# Generate test case data
data = []
serial_number = 1

for series, test_count in series_test_cases.items():
    for test_case in range(1, test_count + 1):
        config_file_number = (test_case % 10) if (test_case % 10) != 0 else 10  # Ensuring 10 instead of 0
        config_file_name = f"Configuration{config_file_number}.xml"
        file_path = os.path.join(rfid_folder_path, config_file_name)

        data.append([serial_number, series, test_case, config_file_name, file_path])
        serial_number += 1  # Increment serial number

# Create DataFrame and Save as CSV
df = pd.DataFrame(data, columns=["Serial Number", "Series Number", "Test Case Number", "Configuration Name", "File Path"])
df.to_csv(csv_file_path, index=False)

print(f"CSV file successfully created at: {csv_file_path}")
