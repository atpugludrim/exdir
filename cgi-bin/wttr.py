import cgi, cgitb
cgitb.enable()

import re
import math
import urllib.parse
import urllib.request

def func():
    location = {"IIT Delhi":"28.545031683577257,77.19041434469378"}
    url = "https://wttr.in/{}".format(location["IIT Delhi"])
    formatting = "%t %h"
    pattern = re.compile(r'(-|\+[\d.]+){}C ([\d.]+)%'.format(chr(176))) 
    rurl = url + '?' + urllib.parse.urlencode({"format":formatting})
    with urllib.request.urlopen(rurl) as resp:
        for line in resp:
            response = line.decode()
    m = pattern.match(response)
    t = float(m.group(1))
    rh = float(m.group(2))
    # dew point calc
    a = 17.625
    b = 243.04
    def f(T,RH):
        return math.log(RH/100) + a * T / (b + T)
    td = b * f(t,rh) / (a - f(t,rh))
    #
    full_format = "%C %t (%f) %h %p %w"
    rurl = url + '?' + urllib.parse.urlencode({"format":full_format})
    with urllib.request.urlopen(rurl) as resp:
        for line in resp:
            weather = line.decode()
    return "IIT Delhi: " + weather + ' Dew point: {:.1f}{}C'.format(td,chr(176))

weather = func()
print("Content-Type: text/html")
print("<html><body><h3>")
print(weather)
print("</h3></body></html>")
