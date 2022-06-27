import sys
import numpy as np

try:
    maxsize = sys.argv[2]
except IndexError:
    maxsize = 5
m,n = np.random.randint(1,maxsize,(2,)).tolist()
grid = np.random.randint(0,2,(m,n))
def grid_maker(p,m,n):
    z = [[0 for _ in range(n)] for k in range(m)]
    for i in range(m):
        for j in range(n):
            r = np.random.rand()
            if r < float(p):
                z[i][j] = 1
    return z
try:
    grid = np.array(grid_maker(sys.argv[3],m,n))
except IndexError:
    pass
with open(f"testcase{sys.argv[1]}.txt","w") as f:
    f.write(f"{m} {n}\n")
    for row in grid:
        for item in row:
            f.write(f"{item} ");
        f.write("\n")
