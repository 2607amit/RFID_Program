import os
import pandas as pd
import shutil
import tkinter as tk
from tkinter import messagebox, ttk
import subprocess

# File paths
csv_file_path = "C:/Documents/amit/csvFile/test_cases.csv"
rfid_in_use_path = "C:/Documents/amit/RFID_File_in_use/Configuration1.xml"
monitor_script_path = "C:/Documents/amit/exe/DummyConfigFileReader.exe"  # Path to the monitoring executable

# Load CSV file
def load_csv():
    return pd.read_csv(csv_file_path)

def get_configuration_file(series, test_case, df):
    row = df[(df['Series Number'] == series) & (df['Test Case Number'] == test_case)]
    if not row.empty:
        return row.iloc[0]['Configuration Name'], row.iloc[0]['File Path']
    return None, None

def update_test_cases(event, series_var, test_case_dropdown, df):
    series = int(series_var.get())
    test_cases = sorted(df[df['Series Number'] == series]['Test Case Number'].unique().tolist())
    test_case_dropdown['values'] = test_cases
    if test_cases:
        test_case_dropdown.current(0)

def restart_monitoring_program():
    try:
        subprocess.run([monitor_script_path], check=True)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to restart monitoring program: {e}")

def check_and_update():
    df = load_csv()
    
    current_series = int(current_series_var.get())
    current_test_case = int(current_test_case_var.get())
    next_series = int(next_series_var.get())
    next_test_case = int(next_test_case_var.get())
    
    current_file, current_path = get_configuration_file(current_series, current_test_case, df)
    next_file, next_path = get_configuration_file(next_series, next_test_case, df)
    
    if current_file and next_file:
        if current_file == next_file:
            messagebox.showinfo("Configuration Status", "No need to change configuration file")
        else:
            if os.path.exists(next_path):
                shutil.copy(next_path, rfid_in_use_path)
                if messagebox.askokcancel("Configuration Updated", "Configuration file has been updated. Restart monitoring?"):
                    restart_monitoring_program()
            else:
                messagebox.showerror("Error", "New configuration file not found!")
    else:
        messagebox.showerror("Error", "Invalid series or test case number.")

# GUI setup
root = tk.Tk()
root.title("KAVACH - RFID Configuration Manager")
root.geometry("400x300")
root.configure(bg="#2E3B55")

frame = tk.Frame(root, padx=20, pady=20, bg="#2E3B55")
frame.pack()

tk.Label(frame, text="RFID Configuration Manager", font=("Arial", 14, "bold"), bg="#2E3B55", fg="white").grid(row=0, columnspan=2, pady=10)

df = load_csv()
series_numbers = sorted(df['Series Number'].unique().tolist())

# Current series & test case
tk.Label(frame, text="Current Series Number:", bg="#2E3B55", fg="white").grid(row=1, column=0, pady=5, sticky="e")
current_series_var = tk.StringVar()
current_series_dropdown = ttk.Combobox(frame, textvariable=current_series_var, values=series_numbers)
current_series_dropdown.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Current Test Case Number:", bg="#2E3B55", fg="white").grid(row=2, column=0, pady=5, sticky="e")
current_test_case_var = tk.StringVar()
current_test_case_dropdown = ttk.Combobox(frame, textvariable=current_test_case_var)
current_test_case_dropdown.grid(row=2, column=1, pady=5)
current_series_dropdown.bind("<<ComboboxSelected>>", lambda event: update_test_cases(event, current_series_var, current_test_case_dropdown, df))

# Next series & test case
tk.Label(frame, text="Next Series Number:", bg="#2E3B55", fg="white").grid(row=3, column=0, pady=5, sticky="e")
next_series_var = tk.StringVar()
next_series_dropdown = ttk.Combobox(frame, textvariable=next_series_var, values=series_numbers)
next_series_dropdown.grid(row=3, column=1, pady=5)

tk.Label(frame, text="Next Test Case Number:", bg="#2E3B55", fg="white").grid(row=4, column=0, pady=5, sticky="e")
next_test_case_var = tk.StringVar()
next_test_case_dropdown = ttk.Combobox(frame, textvariable=next_test_case_var)
next_test_case_dropdown.grid(row=4, column=1, pady=5)
next_series_dropdown.bind("<<ComboboxSelected>>", lambda event: update_test_cases(event, next_series_var, next_test_case_dropdown, df))

# Check & Update button
check_button = tk.Button(frame, text="Check & Update", command=check_and_update, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
check_button.grid(row=5, columnspan=2, pady=10)

root.mainloop()
