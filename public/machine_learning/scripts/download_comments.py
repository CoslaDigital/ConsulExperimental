# Copy a file to a destination with shutil.copyfileobj()
import shutil
import json
import csv

source_file_path = '/home/deploy/consul/current/public/machine_learning/data/comments.json'
source_file = open(source_file_path, 'rb')
destination_file_path = '/home/deploy/consul/current/public/machine_learning/data/ml_comments.json'
csv_file_path = '/home/deploy/consul/current/public/machine_learning/data/ml_comments.csv'
destination_file = open(destination_file_path, 'wb')
shutil.copyfileobj(source_file, destination_file)

def convert_json_to_csv(json_file, csv_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        
        # Write header row
        writer.writerow(data[0].keys())
        
        # Write data rows
        for item in data:
            writer.writerow(item.values())

convert_json_to_csv(source_file_path, csv_file_path)
