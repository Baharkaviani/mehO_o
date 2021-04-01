"""
Created on Thur Apr 1 13:43:00 2020 (1400/1/12)
@author: Bahar Kaviani
"""
import arguments as argu
import sys
sys.path.append("../cmd")
import notification as notif

TIMEOUT = "infinity"

def checkTimeoutArgu(times):
    global TIMEOUT

    if len(times) == 0:
        pass
    elif len(times) == 1:
        TIMEOUT = times[0]
    else:
        notif.warning("timeout")
        TIMEOUT = times[len(times) - 1]

    print("TIMEOUT = {}".format(TIMEOUT))