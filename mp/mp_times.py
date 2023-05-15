import time
from multiprocessing import Process, Manager, Pool
import numpy as np


def f(d, list):
    r = np.random.randint(1,100)
    if r not in d:
        d[r] = list()
    if len(d[r]) == 0:
        d[r].append(0)
    else:
        d[r].append(d[r][-1]+1)


def parallel():
    with Manager() as manager:
        list = manager.list
        d = manager.dict()
        p = []
        for i in range(2000):
            pr = Process(target=f, args=(d,list))
            p.append(pr)
            pr.start()
        for i in range(2000):
            p[i].join()
        d = d.copy()
        d_c = {}
        for k,v in d.items():
            d_c[k] = list(v)
    return d_c


def single():
    d = {}
    for i in range(2000):
        r = np.random.randint(1,100)
        if r not in d:
            d[r] = []
        if len(d[r]) == 0:
            d[r].append(0)
        else:
            d[r].append(d[r][-1]+1)
    return d


def f2(d):
    r = np.random.randint(1,100)
    if r not in d:
        d[r] = []
    d[r].append(len(d[r]))


def f2_drive(i):
    d={}
    f2(d)
    return d


def parallel2():
    with Pool() as pool:
        iterr = pool.imap_unordered(f2_drive, range(2000))
        d_glob={}
        for i in iterr:
            d_glob.update(i)
    return d_glob


def main():
    start = time.perf_counter()
    parallel()
    end = time.perf_counter()
    single()
    end2 = time.perf_counter()
    parallel2()
    end3 = time.perf_counter()
    print(f"Parallel in {end-start:.3f}s and sequential in {end2-end:.3f}s and parallel2 in {end3-end2:.3f}s")
    print("Imap_unordered is much better")


if __name__=="__main__":
    main()
