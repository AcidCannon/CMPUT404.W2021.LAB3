#!/usr/bin/env python3

import os

# Report the user’s browser in the HTML
print("Content-Type: text/html\r\n")
print(f"<p> HTTP_USER_AGENT: {os.environ['HTTP_USER_AGENT']}")