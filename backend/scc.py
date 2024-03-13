from datetime import date, datetime, timedelta
import pyodbc
import pandas as pd
import requests



# URL of the file you want to download
file_url = 'https://cmsprovider.cahwnet.gov/prv/scc.xls'

# Local path to save the downloaded file
file_path = 'D:/Python/scc.xls'

# Download the file
try:
    response = requests.get(file_url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print("File downloaded successfully.")
    else:
        print(f"Failed to download the file. Status code: {response.status_code}")
except Exception as e:
    print(f"An error occurred while downloading the file: {e}")


# Open the file and Read
try:
    with open(file_path, 'r') as file:
        # Skip the first row (header)
        next(file)
        for line in file:
            # Split the line by tabs to get individual values
            values = line.strip().split('\t')
            values = [' ' if val is None else val for val in values]
            values.extend([' ' for _ in range(15 - len(values))])

except Exception as e:
    conn.rollback()
    print(f"An error occurred while inserting data into the SQL Server table: {e}")
