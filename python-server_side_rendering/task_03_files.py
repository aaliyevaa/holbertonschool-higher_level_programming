#!/usr/bin/env python3

from flask import Flask, render_template, request
import json
import csv

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def load_json_data(filepath='products.json'):
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except Exception as e:
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
    except Exception as e:
        return []
    return data

@app.route('/products')
def products():
    source = request.args.get('source')
    id_param = request.args.get('id')
    data = []
    error = None

    if source == 'json':
        data = load_json_data()
    elif source == 'csv':
        data = load_csv_data()
    else:
        error = "Wrong source. Use 'json' or 'csv'."
        return render_template("product_display.html", error=error)

    # Convert id_param to int and filter data
    if id_param:
        try:
            product_id = int(id_param)
            filtered = [item for item in data if item['id'] == product_id]
            if not filtered:
                error = f"Product not found"
                return render_template("product_display.html", error=error)
            return render_template("product_display.html", products=filtered)
        except ValueError:
            error = "Invalid id parameter."
            return render_template("product_display.html", error=error)

    return render_template("product_display.html", products=data)

if __name__ == '__main__':
    app.run(debug=True)


