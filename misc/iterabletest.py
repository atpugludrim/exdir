import argparse
import numpy as np
class A:
    def __init__(this):
        this.someval = 20
    def __iter__(this):
        return class_iter(this)
    def func(this):
        return this.someval
class class_iter:
    def __init__(this, aobj):
        this.Aobj = aobj
        this.idx = 0
    def __iter__(this):
        return this
    def __next__(this):
        if not hasattr(this, 'len'):
            setattr(this, 'len', len(dir(this.Aobj)))
        if this.idx < this.len:
            this.idx += 1
            return dir(this.Aobj)[this.idx-1]
        raise StopIteration

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--numpy','-n',action='store_true',default=False)
    args = parser.parse_args()
    ###########################################################
    for member in A():
        print("A has member {} repr as {}. Callable = {}".format(member,getattr(A(),member),hasattr(getattr(A(),member),'__call__')))

    if args.numpy:
        a = np.random.randint(1,100,(4,))
        for member in class_iter(a):
            print("np.array has member {} repr as {}. Callable = {}".format(member,getattr(a,member),hasattr(getattr(a,member),'__call__')))

if __name__=="__main__":
    main()
