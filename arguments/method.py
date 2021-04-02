"""
Created on Thur Apr 1 16:07:00 2020 (1400/1/12)
@author: Bahar Kaviani
"""
import sys
sys.path.append("../cmd")
import notification as notif

METHOD = "GET"

def checkMethodArgu(methods):
    global METHOD

    if len(methods) == 0:
        pass
    elif len(methods) == 1:
        METHOD = methods[0]
    else:
        notif.warning("method")
        METHOD = methods[len(methods) - 1]

    validity()

    print("METHOD = {}".format(METHOD))

def validity():
    if METHOD == "GET" or METHOD == "POST" or METHOD == "PATCH" or METHOD == "DELETE" or METHOD == "PUT":
        return True
    else:
        notif.wrongMethod()