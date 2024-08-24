import os
import csv

# Path of the folder to read all files and store in csv
directory = 'C:\\Users\\Jamie Beatrice\\Downloads\\misc\\Work'

# Full path for output csv file
output_csv = 'C:\\Users\\Jamie Beatrice\\Downloads\\misc\\Work\\files_list.csv'

try:
    with open(output_csv, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['NUMBER', 'FILENAME'])  # Updated header row
        
        with os.scandir(directory) as entries:
            file_number = 1  # Initialize a counter for numbering files
            
            for entry in entries:
                if entry.is_file():
                    csvwriter.writerow([file_number, entry.name])  # Write the number and file name
                    file_number += 1  # Increment the counter for each file
    
    print(f"CSV file '{output_csv}' created successfully.")
    
    # Confirm the csv file was created
    if os.path.exists(output_csv):
        print(f"Confirmed: CSV file '{output_csv}' exists.")
    else:
        print(f"Error: CSV file '{output_csv}' does not exist after creation.")
except Exception as e:
    print(f"An error occurred: {e}")
