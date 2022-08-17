import time
def memoizer(f):
    vals = {}
    def memoized(x):
        if x not in vals:
            vals[x] = f(x)
        return vals[x]
    return memoized

def f(n):
    if n < 2:
        return n
    else:
        return n + f(n - 1)

f_memoized = memoizer(f)
for k in [20,20,30,30,90,90,200,200]:
    st = time.perf_counter()
    print(F"f({k}): {f_memoized(k)}")
    end = time.perf_counter()
    print(F"{end-st:.8f}s")
