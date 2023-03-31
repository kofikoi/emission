import csv
import json
import os

# Get the path to the data directory
data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')

# Load the CSV file and convert to JSON
with open(os.path.join(data_dir, 'emissions.csv')) as f:
    reader = csv.DictReader(f)
    rows = list(reader)

with open(os.path.join(data_dir, 'emissions.json'), 'w') as f:
    json.dump(rows, f)
