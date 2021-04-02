"""
Created on Fri Apr 2 16:44:00 2020 (1400/1/13)
@author: Bahar Kaviani
"""

import sys
sys.path.append("../cmd")
import notification as notif

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

        for e in hList:
            key, value = e.split(':')

            # select the header with a higher priority (the last one)
            if key in HEADER:
                HEADER[key] = value
                notif.warning("header")
            else:
                HEADER[key] = value

    # print the headers
    print("HEADERS = {}".format(HEADER))