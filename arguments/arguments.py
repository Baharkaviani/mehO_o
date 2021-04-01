"""
Created on Wed Mar 31 12:23:00 2020 (1400/1/11)
@author: Bahar Kaviani
"""

import sys
sys.path.append("../cmd")
import error as err

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

# dictionary of arguments
arguList = {}

def arguMain(input):
    """
    check the url and also manage the arguments
    """
    global URL

    # set the URL
    URL = input[1]

    # check the URL form
    checkURL()

    # collect the arguments
    argumentsPart = input[2:]
    manageArguments(argumentsPart)

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

def manageArguments(allArguments):
    """
    divide all options and merge the same options together
    """
    print("allArguments = {}".format(allArguments))

    # find all method arguments used in the request
    methods = []

    indices = [i for i, a in enumerate(allArguments) if (a == "-M" or a == "--method")]
    for index in indices:
        methods.append(allArguments[index + 1])

    arguList["method"] = methods

    # find all header arguments used in the request
    headers = []

    indices = [i for i, a in enumerate(allArguments) if (a == "-H" or a == "--headers")]
    for index in indices:
        headers.append(allArguments[index + 1])

    arguList["headers"] = headers

    # find all query arguments used in the request
    queries = []

    indices = [i for i, a in enumerate(allArguments) if (a == "-Q" or a == "--queries")]
    for index in queries:
        queries.append(allArguments[index + 1])

    arguList["queries"] = queries

    # find all data sections used in the request
    data = []

    indices = [i for i, a in enumerate(allArguments) if (a == "-D" or a == "--data")]
    for index in data:
        data.append(allArguments[index + 1])

    arguList["data"] = data

    # find all json sections used in the request
    json = []

    indices = [i for i, a in enumerate(allArguments) if (a == "--json")]
    for index in json:
        json.append(allArguments[index + 1])

    arguList["json"] = json

    # find all timeout sections used in the request
    timeout = []

    indices = [i for i, a in enumerate(allArguments) if (a == "--timeout")]
    for index in timeout:
        json.append(allArguments[index + 1])

    arguList["timeout"] = timeout

    print("arguList = {}".format(arguList))