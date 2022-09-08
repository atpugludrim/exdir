# in js:
# Y = f => (x => x(x))(x => f(y => x(x)(y)));
# F = f => (x => (x === 0 ? 1 : x * f(x - 1)));

def Y(f):
    def f_in(x):
        return x(x)
    def f_in2(x):
        def func(y):
            return x(x)(y)
        return f(func)
    return f_in(f_in2)


def F(f):
    def f_in(x):
        if x == 0:
            return 1
        else:
            return x * f(x - 1)
    return f_in

def F2(f):
    def f_in(x):
        if x == 0:
            return 1
        if x == 1:
            return 1
        return f(x-1)+f(x-2)
    return f_in


factorial=Y(F)
maxx = 12
r = list(range(1, maxx+1))


ans = ' '.join(map(str,map(factorial, r)))
print("First",maxx,"factorials are",f"\n{ans}")


maxx = 20
r = list(range(1, maxx+1))
fib=Y(F2)
ans = ' '.join(map(str,map(fib,r)))
print("\nFirst",maxx,"fibonacci numbers are",f"\n{ans}")
