#!/usr/bin/env python3

print("Content-Type: text/html\r\n")
print("""
<h1> Post </h1>
Input something below, and click post button to see what will happen next :)
<form method="POST" action="posted.py">
    <label> <span>key1:</span> <input autofocus type="text" name="key1"></label> <br>
    <label> <span>key2:</span> <input type="text" name="key2"></label>
    <br>
    <button type="submit"> post! </button>
</form>
""")