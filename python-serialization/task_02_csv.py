#!/usr/bin/env python3
"""Convert CSV data to JSON format"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert CSV file to JSON format. Return True if
    successful"""
    try:
        with open(csv_filename, mode='r', encoding='utf-8')
        as csv_file:
            data = list(csv.DictReader(csv_file))
            data_list = []
            for i in data:
                data_list.append(i)
        with open('data.json', mode='w', encoding='utf-8') as jfile:
            json.dump(data_list, jfile, indent=4)

        return:
            True
    except Exception:
        return False
