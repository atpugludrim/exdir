import re
import numpy as np
from wttr import weather_report

# https://iridl.ldeo.columbia.edu/dochelp/QA/Basic/dewpoint.html
# ^^ There are other more accurate formulae as well
#
# Es = E0 x exp[(L/Rv)x(1/T0-1/T)]
# RH = 100 x E/Es
# => E = RHxEs/100
# E = E0 x exp[(L/Rv)x(1/T0-1/Td)]
# => ln(E/E0) = L/Rv x (1/T0-1/Td)
# => 1/T0-1/Td = Rv/Lxln(E/E0)
# => 1/Td = 1/T0-Rv/Lxln(E/E0)
# => Td = 1/(...)
# T0 = 273K, E0 = 0.611 kPa, L/Rv = 5423K
#
# if humidity > 50%, just use Td = T - [(100-RH)/5]

def dewpoint(T,RH):
    E0 = 0.611 #kPa
    T0 = 273 #K
    L_by_Rv = 5423 #K
    if RH > 50:
        return T - (100 - RH) / 5
    else:
        T = T + 273 # C to K
        Es = E0 * np.exp(L_by_Rv * (1 / T0 - 1 / T))
        E = RH * Es / 100
        Td = 1/(1/T0-1/L_by_Rv*np.log(E/E0)) - 273.15
        return Td

def main():
    locations = {'28.5382306,77.1982495':'New Delhi','Durg':'Durg','Raipur':'Raipur','12.9128499,77.6765519':'Banglore'}
    for loc, name in locations.items():
        wr = weather_report(location={loc:name})
        print(wr[0],end='')
        pattern = re.compile(r'.*?(-|\+[\d.]+).*?([\d.]+%)')
        m = pattern.match(wr[1])
        T = float(m.group(1))
        RH = float(m.group(2)[:-1])
        Td = dewpoint(T,RH)
        if Td > 18:
            string = 'sticky'
        else:
            string = 'pleasant'
        print(wr[1],'Dew point:',"{:.3f}".format(Td),string)

if __name__=="__main__":
    main()
