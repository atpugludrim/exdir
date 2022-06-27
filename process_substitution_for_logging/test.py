print("Wow")
print("Line 2")
try:
    raise ValueError
except ValueError as e:
    raise NameError("Wowza")
