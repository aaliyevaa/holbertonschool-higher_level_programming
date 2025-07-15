#!/usr/bin/env python3

from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def load_json_data(filepath='products.json'):
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except Exception:
        return []

def load_csv_data(filepath='products.csv'):
    data = []
    try:
        with open(filepath, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append({
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                })
    except Exception:
        return []
    return data

def load_sql_data(db_path='products.db'):
    data = []
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row  # To access columns by name
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Products')
        rows = cursor.fetchall()
        for row in rows:
            data.append({
                'id': row['id'],
                'name': row['name'],
                'category': row['category'],
                'price': row['price']
            })
        conn.close()
    except Exception:
        return None
    return data

@app.route('/products')
def products():
    source = request.args.get('source')
    id_param = request.args.get('id')
    error = None
    data = []

    if source == 'json':
        data = load_json_data()
    elif source == 'csv':
        data = load_csv_data()
    elif source == 'sql':
        data = load_sql_data()
        if data is None:
            error = "Database error occurred."
            return render_template("product_display.html", error=error)
    else:
        error = "Wrong source. Use 'json', 'csv', or 'sql'."
        return render_template("product_display.html", error=error)

    if id_param:
        try:
            product_id = int(id_param)
            filtered = [item for item in data if item['id'] == product_id]
            if not filtered:
                error = "Product not found"
                return render_template("product_display.html", error=error)
            return render_template("product_display.html", products=filtered)
        except ValueError:
            error = "Invalid id parameter."
            return render_template("product_display.html", error=error)

    return render_template("product_display.html", products=data)

if __name__ == '__main__':
    app.run(debug=True)

