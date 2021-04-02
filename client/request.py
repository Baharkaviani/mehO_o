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
import timeout as timeoutFile
import header as headerFile

def send():
    """
    organize and send the request to server
    """

    # step 1: prepare the message to send

    # step 2: identify the method and send the request

    selectedMethod(methodFile.METHOD)

def selectedMethod(method):
    """
    choose the correct action depend on method
    then send the request to the server
    """
    try:
        switcher = {
            "GET": requests.get(argu.URL,
                                headers = headerFile.HEADER,
                                timeout = timeoutFile.TIMEOUT),
            "POST": requests.post(argu.URL,
                                headers = headerFile.HEADER,
                                timeout = timeoutFile.TIMEOUT),
            "PATCH": requests.patch(argu.URL,
                                headers = headerFile.HEADER,
                                timeout = timeoutFile.TIMEOUT),
            "DELETE": requests.delete(argu.URL,
                                headers = headerFile.HEADER,
                                timeout = timeoutFile.TIMEOUT),
            "PUT": requests.put(argu.URL,
                                headers = headerFile.HEADER,
                                timeout = timeoutFile.TIMEOUT)
        }

        x = switcher.get(method)
        print(x.text)

    except requests.exceptions.Timeout:
        notif.connectionTimeout(argu.URL)