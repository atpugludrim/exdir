import sys
from scipy.special import gamma
import signal
import numpy as np


def handler(signum, frame):
    print('Exiting\n')
    sys.exit()


def fact():
    m = {}
    def f(x):
        x = int(x)
        if x not in m:
            f_ = f(x-1) * x
            m[x] = f_
        return m[x]
    m[0] = 1
    return f


def f(N):
    def g(x):
        s = 1
        for k in range(1, N+1):
            s *= 1/(x/k+1)
        intpart = int(x)
        frcpart = x - intpart
        for k in range(intpart):
            s *= N
        s *= np.power(N, frcpart)
        return s
    return g


def main():
    signal.signal(signal.SIGINT, handler)
    try:
        N = int(sys.argv[1])
    except BaseException as e:
        N = 10000
    g = f(N)
    factorial = fact()
    gammaf = False
    while True:
        x = input("Enter x: ")
        if x == 'q' or x == 'Q':
            handler(0, 0)
        if x == 'g' or x == 'G':
            gammaf = not gammaf
            x = input("Enter x: ")
        x = float(x)
        if np.abs(int(x) - x) != 0:
            gammaf = True
        gx = g(x)
        if gammaf:
            fx = gamma(x+1)
            diff = np.abs(fx-gx)/fx*100
            print(f"{g(x) = :.5f}, factorial(x) = {fx:.5f}, err% = {diff:.2f}")
        else:
            fx = factorial(x)
            diff = np.abs(fx-gx)/fx*100
            print(f"{g(x) = :.2f}, factorial(x) = {fx}, err% = {diff:.2f}")


if __name__=="__main__":
    main()
