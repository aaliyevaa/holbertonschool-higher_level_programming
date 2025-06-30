#!/usr/bin/env python3
"""Convert CSV data to JSON format"""
import csv
import json


def convert_csv_to_json(filename):
    """Convert CSV file to JSON format. Return True if
    successful"""
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            data = csv.DictReader(file)
            data_list = [row for row in data]

        with open('data.json', mode='w', encoding='utf-8') as j:
            json.dump(data_list, j, indent=4)
        return True
    except Exception:
        return False
