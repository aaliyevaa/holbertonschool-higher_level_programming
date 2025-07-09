#!/usr/bin/python3
"""Take in a URL, send a request and display
the value of the X-Request-Id"""
from urllib import request
import sys

if __name__ == "__main__":
    """Ensure code runs when directly run"""
    url = sys.argv[1]
    req = request.Request(url)
    req.add_header("cfclearance", "true")

    with request.urlopen(req) as response:
        """Access the header"""
        header = response.getheader("X-Request-Id")

    print(header)
