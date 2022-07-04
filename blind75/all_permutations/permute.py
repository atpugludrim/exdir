import numpy as np

class counter:
    def __init__(this):
        this.ctr = 0
    def __next__(this):
        this.ctr += 1
        return str(this.ctr)
    def __iter__(this):
        return this

ctr = counter()
def each_line_yielder(lol):
    global ctr
    if isinstance(lol,(list,np.ndarray)):
        for item in lol:
            yield from each_line_yielder(item)
        yield 'linum: {}\n'.format(next(ctr))
    else:
        yield '{} '.format(lol)

this_answer = []
set_bits = []
def permutations(arr, answer=[]):
    global this_answer, set_bits
    if all(set_bits):
        answer.append([k for k in this_answer])
        return
    for idx, (flag, value) in enumerate(zip(set_bits, arr)):
        if not flag:
            this_answer.append(value)
            set_bits[idx] = True
            permutations(arr)
            this_answer.pop()
            set_bits[idx] = False
    return answer
def permute(arr):
    # this will be a wrapper
    global set_bits
    set_bits = [False for _ in range(len(arr))]
    answer = permutations(arr)
    return answer

l = np.random.randint(1,7)
arr = np.arange(0,l)
# arr = [1,2,3]
print(arr)
answer = permute(arr)
print(''.join(each_line_yielder(answer)),end='')
