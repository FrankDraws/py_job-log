from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/log_data', methods=['POST'])
def log_data():
    data = request.json

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

    return jsonify({'message': 'Data logged successfully.'})

if __name__ == "__main__":
    app.run(debug=True)
