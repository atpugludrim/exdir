import numpy as np
import sys
from time import perf_counter
np.random.seed(int(sys.argv[1]))
class nullnodes:
    def __init__(this, par, typ):
        this.par = par
        this.type = typ
        this.val = "nullnode"
    def __repr__(this):
        return this.val+" "+this.type


class heapnode:
    def __init__(this, val, par=None, left=None, right=None):
        this.val = val
        if par == None:
            par = nullnodes(None, 'par')
        this.par = par
        if left == None:
            left = nullnodes(this,'left')
        this.left = left
        if right == None:
            right = nullnodes(this,'right')
        this.right = right
    def getchildren(this):
        return this.left, this.right
    def getval(this):
        return this.val
    def __repr__(this):
        return "{} {} {} {}".format(this.par.val,this.val,this.left.val,this.right.val)


def minheapify(node):
    left, right = node.getchildren()
    if not isinstance(left,nullnodes) and left.val < node.val:
        smallest = left
    else:
        smallest = node
    if not isinstance(right,nullnodes) and right.val < smallest.val:
        smallest = right
    if smallest != node:
        tmp = node.val
        node.val = smallest.val
        smallest.val = tmp
        minheapify(smallest)


def bfsinsert(root, new):
    Q = [root]
    def bfs(new):
        nonlocal Q
        while Q:
            curr = Q.pop(0)
            if isinstance(curr,nullnodes):
                typ = curr.type
                par = curr.par
                if typ == 'left':
                    par.left = new
                    new.par = par
                    break
                elif typ == 'right':
                    par.right = new
                    new.par = par
                    break
            Q.extend(curr.getchildren())
    bfs(new)


# def buildheap(arr):
#     root = heapnode(arr[0])
#     nodes = [root]
#     for i in range(1,len(arr)):
#         newnode = heapnode(arr[i])
#         bfsinsert(root, newnode)
#         nodes.append(newnode)
#     while nodes:
#         curr = nodes.pop()
#         minheapify(curr)


def getkmax(arr, k):
    inserted = 1
    idx = 1
    root = heapnode(arr[0])
    nodes = [root]
    while inserted < k and inserted < len(arr):
        newnode = heapnode(arr[idx])
        bfsinsert(root, newnode)
        nodes.append(newnode)
        idx += 1
        inserted += 1
    while nodes:
        curr = nodes.pop()
        minheapify(curr)
    while idx < len(arr):
        if arr[idx] > root.val:
            root.val = arr[idx]
            minheapify(root)
        idx += 1
    return root


def print_dfs_tree(root):
    Q = [root]
    printvals = []
    def dfs():
        nonlocal Q
        while Q:
            curr = Q.pop()
            if not isinstance(curr, nullnodes):
                printvals.append(curr.val)
                Q.extend(curr.getchildren())
    dfs()
    print(np.sort(printvals))


minval = 1
maxval = 10000
arrlen = 400
k = 20
arr = np.random.randint(minval,maxval,(arrlen,))
print(arr)
t_start = perf_counter()
root = getkmax(arr,k)
t_end = perf_counter()
print_dfs_tree(root)
print(np.sort(arr)[-k:])
print(t_end - t_start)
