#!/usr/bin/env python3
import os
import json

# Serve the environment back as JSON
print("Content-Type: application/json\r\n")
print(json.dumps(dict(os.environ), indent=2))