#!/usr/bin/env python3

import socket
import requests

def check_localhost():
    localhost = socket.gethostbyname("localhost")
    print("Localhost identified: {}".format(localhost))
    return localhost == '127.0.0.1'

def check_connectivity():
    request = requests.get("http://www.google.com")
    response = request.status_code
    print("http Response status code: {}".format(response))
    return response == 200


check_localhost()
check_connectivity()