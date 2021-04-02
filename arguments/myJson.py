"""
Created on Fri Apr 2 20:37:00 2020 (1400/1/13)
@author: Bahar Kaviani
"""

import sys
sys.path.append("../cmd")
import notification as notif
import header as headerFile

JSON = None

def checkJsonArgu(json):
    """
    update and check headers
    """
    global JSON

    # select and set json with a higher priority (the last one)
    if len(json) == 0:
        pass
    elif len(json) == 1:
        JSON = json[0]
    else:
        notif.warning("json")
        JSON = json[len(json) - 1]

    # check if we have not and content-type header
    ifReplaceable()

    # print the timeout
    print("JSON = {}".format(JSON))

def ifReplaceable():
    """
    check the json witch has the higher priority
    then set the json to "content-type" header with "application/json" value
    """
    if headerFile.HEADER.get("content-type") == None:
        headerFile.HEADER["content-type"] = "application/json"
    else:
        notif.warning("priority json")