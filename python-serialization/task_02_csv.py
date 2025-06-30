#!/usr/bin/env python3
"""Convert CSV data to JSON format"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert CSV file to JSON format. Return True if
    successful"""
    try:
        with open(csv_filename, mode='r', newline='',
                  encoding='utf-8') as csv_file:
            data = list(csv.DictReader(csv_file))
        with open('data.json', mode='w', encoding='utf-8') as jfile:
            json.dump(data, jfile, indent=4)

        return:
            True
    except Exception:
        return False
