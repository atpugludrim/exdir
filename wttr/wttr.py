import urllib.request
import urllib.parse
import random

def weather_report(location=None,print_=False):
    if location is None:
        location = {'28.5363,77.1975':'New Delhi','Durg':'Durg','Raipur':'Raipur'}
    loc_idx = random.randint(0, len(location) - 1)
    loc = list(location.keys())[loc_idx]
    if not print_:
        retvar = [' {}: '.format(location[loc])]
    else:
        print(' {}: '.format(location[loc]),end='')
    url = 'http://wttr.in/{}'.format(loc)
    formatting = '%C %t(%f) %w %p %h'
    url = url+'?'+urllib.parse.urlencode({'format':formatting})
    with urllib.request.urlopen(url) as f:
        for j in f:
            if print_:
                print(j.decode())
            else:
                retvar.append(j.decode())
    if not print_:
        return retvar

def main():
    weather_report(print_=True)

if __name__=="__main__":
    main()
