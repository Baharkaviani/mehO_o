"""
Created on Tue Mar 30 23:42:00 2020 (1400/1/10)
@author: Bahar Kaviani
"""
import sys
sys.path.append("../arguments")
import arguments as argu
import error as err

def main():
    """
    check if the user starts the request or not
    """
    the_string = input()
    command, url = the_string.split()

    # check the command
    if command == "meh":
        argu.arguMain()
    else:
        err.wrongCommand(command)

if __name__ == '__main__':
    main()
