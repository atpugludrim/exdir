class Maybe:
    def __init__(this, val=None):
        this.val = val
        this.isValid()
    def isValid(this):
        if this.val is None:
            this.valid = False
        else:
            this.valid = True
        return this.valid
    def Value(this):
        return this.val
    @staticmethod
    def fmap(f):
        def f_interior(x: Maybe) -> Maybe:
            if x.isValid():
                value = x.Value()
                try:
                    returned = f(value)
                except BaseException:
                    return Maybe()
                else:
                    return Maybe(returned)
            else:
                return Maybe()
        return f_interior
    def __repr__(this):
        if this.isValid():
            return f"{this.Value()}"
        else:
            return "<INVALID>"

# f:: Float->Float->Float
# f'::Float->Maybe Float->Maybe Float
# the second part of the curry is lifted using fmap
def division(a):
    def f(b):
        return a / b
    return f

# f::Float->Float->Maybe Float
def div_maybe(a):
    def f(b):
        ret = Maybe()
        try:
            ret = Maybe(a/b)
        except BaseException:
            pass
        return ret
    return f

a = float(input("a: "))
b = float(input("b: "))
fdiv = Maybe.fmap(division(a))
print(f"{fdiv(Maybe(b)) = }")
print(f"{div_maybe(a)(b) = }")
