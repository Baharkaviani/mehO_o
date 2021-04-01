"""
Created on Wed Mar 31 12:23:00 2020 (1400/1/11)
@author: Bahar Kaviani
"""

import sys
sys.path.append("../cmd")
import error as err

### global variables
# URL parts
URL = None
SCHEME = None
USER = None
PASS = None
HOST = None
PORT = None
PATH = None
QUERY = None
FRAG = None

def arguMain(input):
    """
    """

    # set the URL
    global URL
    URL = input[1]

    # check the URL form
    checkURL()


def checkURL():
    """
    check whether the first argument is a correct url
    """
    global URL, SCHEME, USER, PASS, HOST, PORT, PATH, QUERY, FRAG

    # check the scheme
    try:
        SCHEME, rest = URL.split("://")
    except ValueError:
        #print("the protocol of request isn't specified")
        err.wrongURL()

    # check if url has user and pass or not
    try:
        userPass, rest = rest.split('@')
        USER, PASS = userPass.split(':')
    except ValueError:
        #print("no user pass in url")
        pass

    # check if url has host and port section or not
    try:
        hostPort, rest = rest.split('/')

        try:
            HOST, PORT = hostPort.split(':')
        except ValueError:
            rest = hostPort + '/' + rest
            #print("no host port in url")

    except ValueError:
        #print("no host port in url")
        pass

    # check the path
    try:
        PATH, rest = rest.split('?')
    except ValueError:
        if rest != "":
            PATH = rest
            rest = ""
        else:
            #print("url has no path")
            err.wrongURL()


    # check query and frag sections
    try:
        QUERY, FRAG = rest.split('#')
    except ValueError:
        if rest != "":
            QUERY = rest

    print("SCHEME = {}".format(SCHEME))
    print("USER = {}, PASS = {}".format(USER, PASS))
    print("HOST = {}, PORT = {}".format(HOST, PORT))
    print("PATH = {}".format(PATH))
    print("QUERY = {}".format(QUERY))
    print("FRAG = {}".format(FRAG))
