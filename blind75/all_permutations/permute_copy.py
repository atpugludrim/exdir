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

class Solution:
    def __init__(this):
        this.this_answer = []
        this.set_bits = []
        this.answer = []
    def permutations(this, arr):
        if all(this.set_bits):
            this.answer.append([k for k in this.this_answer])
            return
        for idx, (flag, value) in enumerate(zip(this.set_bits, arr)):
            if not flag:
                this.this_answer.append(value)
                this.set_bits[idx] = True
                this.permutations(arr)
                this.this_answer.pop()
                this.set_bits[idx] = False
        return this.answer
    def permute(self, nums):
        self.set_bits = [False for _ in range(len(nums))]
        answer = self.permutations(nums)
        self.answer = []
        return answer

l = np.random.randint(1,7)
arr = np.arange(0,l)
# arr = [1,2,3]
print(arr)
answer = Solution().permute(arr)
print(''.join(each_line_yielder(answer)),end='')
