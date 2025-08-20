import csv
import os

def save_to_csv(data, filename):
    print(f"Debug: Original filename: {filename}")  # Debug log

    # Ensure the filename has a .csv extension
    if not filename.endswith(".csv"):
        filename += ".csv"
        print(f"Debug: Updated filename with .csv extension: {filename}")  # Debug log

    # Ensure the directory exists, even if no directory is specified
    directory = os.path.dirname(filename)
    if directory:  # Only create directories if a directory is specified
        os.makedirs(directory, exist_ok=True)

    file_exists = os.path.isfile(filename)

    with open(filename, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "job_title", "location"])
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)
    
    print(f"✅ Data successfully written to {filename}")  # Confirmation message