import sys
import numpy as np

try:
    maxsize = sys.argv[2]
except IndexError:
    maxsize = 5
m,n = np.random.randint(1,maxsize,(2,)).tolist()
grid = np.random.randint(0,2,(m,n))
with open(f"testcase{sys.argv[1]}.txt","w") as f:
    f.write(f"{m} {n}\n")
    for row in grid:
        for item in row:
            f.write(f"{item} ");
        f.write("\n")
