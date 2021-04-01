"""
Created on Tue Mar 30 23:42:00 2020 (1400/1/10)
@author: Bahar Kaviani
"""
import sys
sys.path.append("../arguments")
import arguments as argu
import notification as notif

def main():
    """
    check if the user starts the request or not
    """
    inp = list(input().split())
    command = inp[0]

    # check the command
    if command == "meh":
        argu.arguMain(inp)
    else:
        notif.wrongCommand(command)

if __name__ == '__main__':
    main()
