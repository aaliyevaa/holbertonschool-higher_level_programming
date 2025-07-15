#!/usr/bin/env python3

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json():
    try:
        with open('products.json') as f:
            return json.load(f)
    except:
        return []

def read_csv():
    try:
        with open('products.csv') as f:
            reader = csv.DictReader(f)
            return list(reader)
    except:
        return []

@app.route('/products')
def products():
    source = request.args.get('source')
    id_param = request.args.get('id')
    error = None
    products = []

    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    else:
        error = "Wrong source"

    # Filter by ID if provided
    if not error and id_param:
        try:
            products = [p for p in products if str(p.get("id")) == str(id_param)]
            if not products:
                error = "Product not found"
        except:
            error = "Error filtering products"

    return render_template("product_display.html", products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)


