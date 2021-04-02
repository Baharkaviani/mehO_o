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
import query as queryFile
import data as dataFile
import myJson as jsonFile

def selectedMethod():
    """
    organize and send the request to server
    choose the correct action depend on method
    """
    method = methodFile.METHOD

    try:
        switcher = {
            "GET": requests.get(argu.URL,
                                headers = headerFile.HEADER,
                                params  = queryFile.QUERY,
                                timeout = timeoutFile.TIMEOUT),
            "POST": requests.post(argu.URL,
                                headers = headerFile.HEADER,
                                json    = dataFile.DATA,
                                data    = jsonFile.JSON,
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