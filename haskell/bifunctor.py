import math
import random


def bifunctor(typea, typeb):
    def f(a, b):
        assert isinstance(a, typea) and isinstance(b, typeb)
        return (a,b)
    return f


def bimap(f, g, typec, typed):
    def ret(ab_tuple):
        a, b = ab_tuple
        c = f(a)
        d = g(b)
        functor = bifunctor(typec, typed)
        return functor(c,d)
    return ret


def compose(f, g):
    def ret(x):
        return g(f(x))
    return ret


def main():
    typea = int
    typeb = bool
    functor = bifunctor(typea, typeb)
    #-------------------------------
    def divby(n: int):
        print(F"divby {n}")
        def f(a: int) -> float:
            return a / n
        return f
    def g(b: bool) -> int:
        if b:
            return 1
        else:
            return 0
    def i(d: float) -> str:
        return "{:.3f}".format(d)
    def j(e: float) -> float:
        r"""exp(e)
        """
        fact_cache = dict()
        fact_cache[0] = 1
        fact_cache[1] = 1
        fact_cache[2] = 2
        def fact(n):
            if n not in fact_cache:
                fact_cache[n] = n * fact(n - 1)
            return fact_cache[n]
        retval = 0.0
        for k in range(100):
            retval += math.pow(e, k) / fact(k)
        return retval
    #-------------------------------
    typec = str
    typed = str
    print("f is ", end='')
    f = divby(random.randint(2,15))
    print("h is ", end='')
    h = divby(random.randint(2,15))
    fgmapped = bimap(compose(compose(f, j), i), compose(compose(g, h), i), typec, typed)
    #-------------------------------
    a = -3
    b = True
    ab_product = functor(a, b)
    #-------------------------------
    returned = fgmapped(ab_product)
    print(f"Thin wrapper around {typec, typed} returned by bifunctor = {returned}")


if __name__=="__main__":
    main()
