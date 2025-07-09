#!/usr/bin/python3
""" POST request to the passed URL"""
from urllib import request, parse
import sys

if __name__ == "__main__":
    """Ensure the code is executed when directly run"""
    url = sys.argv[1]
    email = sys.argv[2]
    email = parse.urlencode({'email': email}).encode('utf-8')
    req = request.Request(url)
    req.add_header("cfclearance", "true")

    with request.urlopen(req, data=email) as response:
        """ Opens the URL"""
        body = response.read().decode('utf-8')
        print(body)
