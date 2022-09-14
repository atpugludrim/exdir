def f1(b):
    if b >= 0 and b <= 127:
        return 1
    elif b >= 192 and b <= 223:
        return 2
    elif b >= 224 and b <= 239:
        return 3
    elif b >= 240 and b <= 247:
        return 4
    else:
        return -1


def f2(bs):
    return list(map(f3, bs))


def f3(b):
    if b >= 128 and b <= 191:
        return True
    else:
        return False


def main():
    bs = list(map(int,input("Sequence of bytes please: ").split()))
    start = 0
    end = len(bs)
    #import pdb;pdb.set_trace()
    while True:
        head = bs[start]
        n = f1(head)
        if n == -1:
            return False
        if n == 1:
            start = start + 1
            if start >= len(bs):
                break
            continue
        end = start + n
        bs_sub = bs[start + 1: end]
        if len(bs_sub) < (n - 1):
            return False
        if not all(f2(bs_sub)):
            return False
        start = start + n
        if start >= len(bs):
            break
    return True


if __name__=="__main__":
    print(main())
