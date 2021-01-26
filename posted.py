#!/usr/bin/env python3

import os
import sys
import templates
import secret

posted_bytes = os.environ.get("CONTENT_LENGTH", 0)
if posted_bytes:
    print("Content-Type: text/html\r\n")
    posted = sys.stdin.read(int(posted_bytes))
    print(f"<h1> Post </h1>")
    print("POSTED:")
    for line in posted.splitlines():
        print(line)
        for each in line.split("&"):
            (key, value) = each.split("=")
            print(f"<li><em>{key}</em> = {value}</li>")
