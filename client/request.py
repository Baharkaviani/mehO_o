"""
Created on Fri Apr 2 14:25:00 2020 (1400/1/13)
@author: Bahar Kaviani
"""

import sys
import requests
sys.path.append("../cmd")
sys.path.append("../arguments")
import notification as notif
import arguments as argu
import method as methodFile

def send():
    """
    organize and send the request to server
    """

    # step 1: prepare the message to send


    # step 2: identify the method and send the request
    selectedMethod(methodFile.METHOD)

def selectedMethod(method):
    switcher = {
        "GET": requests.get(argu.URL),
        "POST": requests.post(argu.URL),
        "PATCH": requests.patch(argu.URL),
        "DELETE": requests.delete(argu.URL),
        "PUT": requests.put(argu.URL)
    }
    x = switcher.get(method)
    print(x.text)
