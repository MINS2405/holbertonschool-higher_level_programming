#!/usr/bin/python3

import csv
import json

def convert_csv_to_json(csv_filename):
    try:
        # Read CSV data
        with open(csv_filename, mode='r', newline='', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        # Write JSON data
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except Exception:
        return False
