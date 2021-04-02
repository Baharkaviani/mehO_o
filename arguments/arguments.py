"""
Created on Wed Mar 31 12:23:00 2020 (1400/1/11)
@author: Bahar Kaviani
"""

import sys
sys.path.append("../cmd")
import notification as notif
import timeout as timeFile
import method as methodFile

# URL parts
URL = None

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
    scheme = None
    user = None
    password = None
    host = None
    port = None
    path = None
    urlQuery = None
    frag = None
    global URL

    # check the scheme
    try:
        scheme, rest = URL.split("://")
    except ValueError:
        #print("the protocol of request isn't specified")
        notif.wrongURL()

    # check if url has user and pass or not
    try:
        userPass, rest = rest.split('@')
        user, password = userPass.split(':')
    except ValueError:
        #print("no user pass in url")
        pass

    # check if url has host and port section or not
    try:
        hostPort, rest = rest.split('/')

        try:
            host, port = hostPort.split(':')
        except ValueError:
            rest = hostPort + '/' + rest
            #print("no host port in url")

    except ValueError:
        #print("no host port in url")
        pass

    # check the path
    try:
        path, rest = rest.split('?')
    except ValueError:
        if rest != "":
            path = rest
            rest = ""
        else:
            #print("url has no path")
            notif.wrongURL()


    # check query and frag sections
    try:
        urlQuery, frag = rest.split('#')
    except ValueError:
        if rest != "":
            urlQuery = rest

    print("SCHEME = {}".format(scheme))
    print("USER = {}, PASS = {}".format(user, password))
    print("HOST = {}, PORT = {}".format(host, port))
    print("PATH = {}".format(path))
    print("QUERY = {}".format(urlQuery))
    print("FRAG = {}".format(frag))

def manageArguments(allArguments):
    """
    divide all options and merge the same options together
    """
    #print("allArguments = {}".format(allArguments))

    # find all method arguments used in the request
    methods = []

    indices = [i for i, a in enumerate(allArguments) if (a == "-M" or a == "--method")]
    for index in indices:
        methods.append(allArguments[index + 1])

    arguList["method"] = methods

    methodFile.checkMethodArgu(arguList.get("method"))

    # find all header arguments used in the request
    headers = []

    indices = [i for i, a in enumerate(allArguments) if (a == "-H" or a == "--headers")]
    for index in indices:
        headers.append(allArguments[index + 1])

    arguList["headers"] = headers

    # find all query arguments used in the request
    queries = []

    indices = [i for i, a in enumerate(allArguments) if (a == "-Q" or a == "--queries")]
    for index in indices:
        queries.append(allArguments[index + 1])

    arguList["queries"] = queries

    # find all data sections used in the request
    data = []

    indices = [i for i, a in enumerate(allArguments) if (a == "-D" or a == "--data")]
    for index in indices:
        data.append(allArguments[index + 1])

    arguList["data"] = data

    # find all json sections used in the request
    json = []

    indices = [i for i, a in enumerate(allArguments) if (a == "--json")]
    for index in indices:
        json.append(allArguments[index + 1])

    arguList["json"] = json

    # find all timeout sections used in the request
    timeout = []

    indices = [i for i, a in enumerate(allArguments) if (a == "--timeout")]
    for index in indices:
        timeout.append(allArguments[index + 1])

    arguList["timeout"] = timeout

    timeFile.checkTimeoutArgu(arguList.get("timeout"))

    print("arguList = {}".format(arguList))