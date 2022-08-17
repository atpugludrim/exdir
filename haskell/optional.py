import math


def getOptional(a):
    class optional:
        def __init__(this, value=None):
            if value is None:
                this.is_valid = False
                this.value = value
            else:
                if isinstance(value, a):
                    this.is_valid = True
                    this.value = value
                else:
                    this.is_valid = False
                    this.value = None
        def isValid(this):
            return this.is_valid
        def Value(this):
            return this.value
        def __repr__(this):
            if this.isValid():
                return f"{this.Value()}"
            else:
                return "invalid"
    return optional


def safe_root(x):
    if not isinstance(x, (float, int)):
        return getOptional(float)()
    if x >= 0:
        return getOptional(float)(math.sqrt(x))
    else:
        return getOptional(float)()


opt_int = getOptional(int)
obj = opt_int(value=12)
print(""">>> opt_int = getOptional(int)
>>> obj = opt_int(value=12)
>>> print(obj)""")
print(obj)

print(">>> safe_root(-12), safe_root(12)")
print(f"({safe_root(-12)}, {safe_root(12)})")

# Kleisli category for Optional
# type Optional a = (Bool, a)
# (>=>) :: (a -> Optional b) -> (b -> Optional c) -> (a -> Optional c)
# (>=>) m1 m2 = \x ->
#   let (valid, value) = x
#       if not valid return Optional(False, None)
#       else
#           (valid, value) = m1 x
#           if not valid return Optional(False, None)
#           else
#               return m2 x
# id :: a -> Optional a
# id x = Optional(True, x)


def safe_reciprocal(x):
    if not isinstance(x, (int, float)):
        return getOptional(float)()
    if x != 0:
        return getOptional(float)(1/x)
    else:
        return getOptional(float)()


def fish(m1, m2):
    def f(x):
        r1 = m1(x)
        if not r1.isValid():
            return r1
        else:
            r2 = m2(r1.Value())
            return r2
    return f


safe_root_reciprocal = fish(safe_reciprocal, safe_root)
val = float(input(">>> Enter argument for safe_root_reciprocal: "))
print(f">>> safe_root_reciprocal({val})")
print(f"{safe_root_reciprocal(val)}")
print(">>> # The following will fail to typecase user input to float properly")
val = input(">>> Enter argument for safe_root_reciprocal: ")
print(f">>> safe_root_reciprocal({val})")
print(f"{safe_root_reciprocal(val)}")
print(">>> safe_root_reciprocal(5)")
print(f"{safe_root_reciprocal(5)}")
print(">>> safe_root_reciprocal(0)")
print(f"{safe_root_reciprocal(0)}")
print(">>> safe_root_reciprocal(getOptional(int)(5))")
print(f"{safe_root_reciprocal(getOptional(int)(5))}")

print(">>> # The above is now a pure functional as it'll return something for every value it gets as input (different classes are accepted as well.)")
