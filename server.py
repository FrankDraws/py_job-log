from flask import Flask, render_template, request, redirect, url_for
import json
from datetime import datetime

app = Flask(__name__)

# Root/Home
@app.route('/')
def index():
    try:
        with open('data/data.json', 'r') as file:
            job_data = json.load(file)
    except FileNotFoundError:
        job_data = []

    return render_template('index.html', job_data=job_data)

# form.html
@app.route('/form')
def form():
    return render_template('form.html')

# The form itself
@app.route('/log_data', methods=['POST'])
def log_data():
    data = {
        'date': datetime.now().strftime("%B %d, %Y"),
        'company': request.form['company'],
        'position': request.form['position'],
        'description': request.form['description']
    }

    try:
        # Load existing data from JSON file
        with open('data/data.json', 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []  # Initialize empty list if file not found

    # Append new data to existing data
    existing_data.append(data)

    # Write updated data to JSON file
    with open('data/data.json', 'w') as file:
        json.dump(existing_data, file, indent=4)

    return render_template('success.html', message="Job application logged successfully!")

# job-details.html
@app.route('/job-details')
def job_details():
    # ... (logic to retrieve job data if needed)
    job_data = {...}  # Replace with retrieved data
    print(job_data)  # Add this line
    return render_template('job-details.html', job_data=job_data)


if __name__ == "__main__":
    app.run(debug=True)
