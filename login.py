#!/usr/bin/env python3

import os
import sys
import templates
import secret
import http.cookies as ck

auth = {}

# set to False to use http.cookies library
SET_COOKIES_MANUALLY = False


if SET_COOKIES_MANUALLY: 
    # get cookies first
    cookies = os.environ.get("HTTP_COOKIE").strip("auth").strip("=")
    if cookies:
        # parse
        for cookie in cookies.split("&"):
            (key, value) = cookie.split("=")
            if key not in auth.keys():
                auth[key] = value
        auth_keys = auth.keys()
        if "username" in auth_keys and "password" in auth_keys:
            # this means cookies exists, also must mean the username and password are valid
            print("Content-Type: text/html\r\n")
            print(templates.secret_page(auth["username"], auth["password"]))
    # cannot find cookies
    else:
        # get username and password from POST request then
        posted_bytes = os.environ.get("CONTENT_LENGTH", 0)
        if posted_bytes:
            posted = sys.stdin.read(int(posted_bytes))
            for line in posted.splitlines():
                for each in line.split("&"):
                    (key, value) = each.split("=")
                    if key not in auth.keys():
                        auth[key] = value
        auth_keys = auth.keys()
        if "username" in auth_keys and "password" in auth_keys:
            if auth["username"] == secret.username and auth["password"] == secret.password:
                # send cookies if and only if username and password are valid
                print(f"Set-Cookie: auth=username={auth['username']}&password={auth['password']}")
                print("Content-Type: text/html\r\n")
                print(templates.secret_page(auth["username"], auth["password"]))
            else:
                print("Content-Type: text/html\r\n")
                print(templates.after_login_incorrect())
else:
    # get cookies first
    cookies = ck.SimpleCookie(os.environ.get("HTTP_COOKIE"))
    if cookies:
        cookies_keys = cookies.keys()
        if "username" in cookies_keys and "password" in cookies_keys:
            # this means cookies exists, also must mean the username and password are valid
            print("Content-Type: text/html\r\n")
            print(templates.secret_page(cookies["username"].value, cookies["password"].value))
    else:
        # get username and password from POST request then
        posted_bytes = os.environ.get("CONTENT_LENGTH", 0)
        if posted_bytes:
            posted = sys.stdin.read(int(posted_bytes))
            for line in posted.splitlines():
                for each in line.split("&"):
                    (key, value) = each.split("=")
                    if key not in auth.keys():
                        auth[key] = value
        auth_keys = auth.keys()
        if "username" in auth_keys and "password" in auth_keys:
            if auth["username"] == secret.username and auth["password"] == secret.password:
                # send cookies if and only if username and password are valid
                cookies = ck.SimpleCookie()
                cookies["username"] = auth["username"]
                cookies["password"] = auth["password"]
                print(cookies)
                print("Content-Type: text/html\r\n")
                print(templates.secret_page(auth["username"], auth["password"]))
            else:
                print("Content-Type: text/html\r\n")
                print(templates.after_login_incorrect())
