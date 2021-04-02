"""
Created on Wed Mar 31 12:27:00 2020 (1400/1/11)
@author: Bahar Kaviani
"""

def wrongCommand(command):
    print("{} command not found!".format(command))
    exit()

def wrongURL():
    print("The URL is not correct.")
    exit()

def wrongMethod():
    print("The method is not valid.")
    exit()

def connectionTimeout(url):
    print(f"Connection to {url} timed out.")
    exit()

def warning(problem):
    if problem == "timeout":
        print("Warning! the last timeout will be set for your request.")
    if problem == "method":
        print("Warning! the last method will be set for your request.")
    if problem == "header":
        print("Warning! the last header will be set for your request.")
    if problem == "priority data":
        print("Warning! content-type header has higher priority than data argument.")
