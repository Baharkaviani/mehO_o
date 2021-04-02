"""
Created on Fri Apr 2 14:25:00 2020 (1400/1/13)
@author: Bahar Kaviani
"""

import request

def responseLog():
    response = request.RESPONSE

    print("HTTP/{}".format(response.raw.version/10, response.raw.version%10),
          response.status_code,
          response.reason)

    for h in response.headers:
        print("{header}: {value}".format(header = h, value = response.headers.get(h)))