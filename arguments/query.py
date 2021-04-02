"""
Created on Fri Apr 2 18:11:00 2020 (1400/1/13)
@author: Bahar Kaviani
"""

import sys
sys.path.append("../cmd")
import notification as notif

QUERY = {}

def checkQueryArgu(queries):
    """
    set and check queries
    """
    global QUERY

    # collect and merge all queries
    for q in queries:
        try:
            qList = q.split('&')
        except ValueError:
            # q has just one key:value
            qList = q

        # check all queries values for each 'queries' member
        for e in qList:
            key, value = e.split('=')

            # select the query with a higher priority (the last one)
            if key in QUERY:
                notif.warning("query")

            QUERY[key] = value

    # print the queries
    print("QUERIES = {}".format(QUERY))