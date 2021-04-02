"""
Created on Thur Apr 1 13:43:00 2020 (1400/1/12)
@author: Bahar Kaviani
"""
import sys
sys.path.append("../cmd")
import notification as notif

TIMEOUT = None

def checkTimeoutArgu(times):
    """
    set and check timeout
    """
    global TIMEOUT

    # select and set timeout with a higher priority (the last one)
    if len(times) == 0:
        pass
    elif len(times) == 1:
        TIMEOUT = num(times[0])
    else:
        notif.warning("timeout")
        TIMEOUT = num(times[len(times) - 1])

    # print the timeout
    print("TIMEOUT = {}".format(TIMEOUT))

def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)