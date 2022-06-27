import sys
import numpy as np

def main():
    n = np.random.randint(1,21)
    mat = np.random.randint(-1000,1001,(n,n))
    with open(f"testcase{sys.argv[1]}.txt","w") as f:
        f.write(f"{n}\n")
        for row in mat:
            for item in row:
                f.write(f"{item} ");
            f.write("\n")

if __name__=="__main__":
    main()
