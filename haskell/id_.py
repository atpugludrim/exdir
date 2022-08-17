def id_(x):
    return x
def comp(f, g):
    def com(x):
        return f(g(x))
    return com
def f(x):
    return x+1
c=comp(id_,comp(f,id_))
print(c(5))
