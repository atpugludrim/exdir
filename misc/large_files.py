import os
import time

import sys
from heapq import nlargest


class timer:
    def __enter__(this):
        this.start = time.perf_counter()
    def __exit__(this, *args, **kwargs):
        this.dur = time.perf_counter() - this.start
        print(f"Time taken = {this.dur}s")


def walk(root: str):
    for r, _, files in os.walk(root):
        for f in files:
            path = os.path.join(r, f)
            try:
                size = os.path.getsize(path)
                yield path,size
            except OSError:
                continue

def largest_files(n: int, root: str) -> None:
    largest = nlargest(n, walk(root), key=lambda x: x[1])
    MB = 1024*1024
    for path, size in largest:
        print(f"{size/MB:.2f} MB {path}")


def main():
    try:
        assert len(sys.argv) > 2, f"usage:\n\t$python3 {sys.argv[0]} <.|start-directory> <number-of-largest>"
    except AssertionError as e:
        print(e)
        sys.exit()
    root = os.path.abspath(sys.argv[1])
    assert os.path.isdir(root), f"Not a directory: {root}"
    n = int(sys.argv[2])
    with timer():
        largest_files(n, root)


if __name__ == "__main__":
    main()
