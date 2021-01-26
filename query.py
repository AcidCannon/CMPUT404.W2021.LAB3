#!/usr/bin/env python3
# Report the values of the query parameters in the HTML

import os

print("Content-Type: text/html\r\n")
print("""
    <!doctype html>
    <html>
    <body>
    <h1>Query</h1>""")
print(f"<p> QUERY_STRING: {os.environ['QUERY_STRING']}")
print("<ul>")
for parameter in os.environ["QUERY_STRING"].split("&"):
    (name, value) = parameter.split("=")
    print(f"<li><em>{name}</em> = {value}</li>")
print("""
</ul>
""")