from collections import namedtuple


def init_add():
    cnt = 0
    def add():
        nonlocal cnt
        cnt += 1
    def get():
        return cnt
    Count = namedtuple('Count', ['add', 'get'])
    count = Count(add, get)
    return count


def main():
    count = init_add()
    count.add()
    print(count.get())
    # dir(count), dir(count.add), dir(count.get) <- none of these
    # have any reference to the local variable cnt in init_add.
    # that piece of memory cannot be accessed.
    import pdb;pdb.set_trace()


if __name__=="__main__":
    main()
