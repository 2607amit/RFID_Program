import os
import time
import threading
import tkinter as tk
from tkinter import messagebox

# Path to the RFID file in use
rfid_file_path = "C:/Documents/amit/RFID_File_in_use/Configuration1.xml"

# Function to monitor the file for changes
def monitor_file():
    global last_modified_time
    last_modified_time = os.path.getmtime(rfid_file_path)  # Get initial modified time

    while monitoring:  
        try:
            current_modified_time = os.path.getmtime(rfid_file_path)  # Check file modification time
            if current_modified_time != last_modified_time:
                last_modified_time = current_modified_time
                messagebox.showinfo("File Update", "Configuration1.xml has been modified!")
        except FileNotFoundError:
            messagebox.showerror("Error", "Configuration1.xml not found!")

        time.sleep(2)  # Check every 2 seconds

# Start monitoring in a separate thread
def start_monitoring():
    global monitoring
    monitoring = True
    monitor_thread = threading.Thread(target=monitor_file, daemon=True)
    monitor_thread.start()

# Stop monitoring
def stop_monitoring():
    global monitoring
    monitoring = False
    messagebox.showinfo("Stopped", "File monitoring has been stopped.")

# GUI setup
root = tk.Tk()
root.title("RFID Configuration Monitor")
root.geometry("300x200")
root.configure(bg="#2E3B55")

frame = tk.Frame(root, padx=20, pady=20, bg="#2E3B55")
frame.pack()

tk.Label(frame, text="RFID Configuration Monitor", font=("Arial", 12, "bold"), bg="#2E3B55", fg="white").pack(pady=10)

start_button = tk.Button(frame, text="Start Monitoring", command=start_monitoring, bg="green", fg="white", font=("Arial", 10, "bold"))
start_button.pack(pady=5)

stop_button = tk.Button(frame, text="Stop Monitoring", command=stop_monitoring, bg="red", fg="white", font=("Arial", 10, "bold"))
stop_button.pack(pady=5)

root.mainloop()
