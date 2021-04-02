"""
Created on Fri Apr 2 16:44:00 2020 (1400/1/13)
@author: Bahar Kaviani
"""

import sys
sys.path.append("../cmd")
sys.path.append("../arguments")
import notification as notif
import arguments as argu
import data as dataFile

HEADER = {}

def checkHeaderArgu(headers):
    """
    set and check headers
    """
    global HEADER

    # collect and merge all headers
    for h in headers:
        try:
            hList = h.split(',')
        except ValueError:
            # h has just one key:value
            hList = h

        # check all header values for each 'headers' member
        for e in hList:
            key, value = e.split(':')

            # select the header with a higher priority (the last one)
            if key in HEADER:
                notif.warning("header")

            HEADER[key] = value

    # check data
    dataFile.checkDataArgu(argu.arguList.get("data"))

    # print the headers
    print("HEADERS = {}".format(HEADER))