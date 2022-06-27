import numpy as np
class M:
    def __init__(this, m, n = None):
        this.m = m
        if n != None:
            this.n = n
    def __len__(this):
        return this.m
    def __getitem__(this, idx):
        if not isinstance(idx,int):
            raise TypeError("Only integer indices allowed")
        if idx == 0:
            if hasattr(this, 'n'):
                return M(this.n)
            else:
                raise IndexError
        else:
            raise IndexError("Out of bounds")

def liststrrer(list_,level=0):
    len_ = len(list_)
    for _ in range(level):
        yield ' '
    yield '['
    for idx, item in enumerate(list_):
        if isinstance(item, (list,tuple)):
            if idx != 0:
                yield from liststrrer(item,level+1)
            else:
                yield from liststrrer(item,level)
            if idx != len_ - 1:
                yield '\n'
        else:
            yield repr(item)
            if idx != len_ - 1:
                yield ' '
    yield ']'

matrix = M(3,4)
nonzero_matrix = np.random.randint(1,20,(3,4)).tolist()
zero_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
copied_matrix = [row[:] for row in zero_matrix]
transposed_matrix = zip(*nonzero_matrix)
print(''.join(liststrrer(zero_matrix)))
print(''.join(liststrrer(copied_matrix)))
print(''.join(liststrrer(nonzero_matrix)))
print(''.join(liststrrer(list(transposed_matrix))))
