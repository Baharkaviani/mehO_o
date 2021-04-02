"""
Created on Fri Apr 2 18:50:00 2020 (1400/1/13)
@author: Bahar Kaviani
"""

import sys
sys.path.append("../cmd")
import notification as notif
import header as headerFile

DATA = None

def checkDataArgu(data):
    """
    update and check headers
    """
    global DATA

    # select and set data with a higher priority (the last one)
    if len(data) == 0:
        pass
    elif len(data) == 1:
        DATA = data[0]
    else:
        notif.warning("data")
        DATA = data[len(data) - 1]

    # check if we have not and content-type header
    ifReplaceable()

    # print the timeout
    print("DATA = {}".format(DATA))

def ifReplaceable():
    """
    check the data witch has the higher priority
    then set the data to "content-type" header with "application/x-www-form-urlencoded" value
    """
    if "content-type" in headerFile.HEADER:
        headerFile.HEADER["content-type"] = "application/x-www-form-urlencoded"
    else:
        notif.warning("priority data")
