import json
from datetime import datetime

def log_data():
    data = {}

    # Collect data from user input
    data['Date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data['Company'] = input("Enter the company name: ")
    data['Position'] = input("Enter the position: ")
    data['Description'] = input("Enter a description: ")

    # Load existing data from JSON file
    try:
        with open('data.json', 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []

    # Append new data to existing data
    existing_data.append(data)

    # Write updated data to JSON file
    with open('data.json', 'w') as file:
        json.dump(existing_data, file, indent=4)

    print("Data logged successfully.")

if __name__ == "__main__":
    log_data()
