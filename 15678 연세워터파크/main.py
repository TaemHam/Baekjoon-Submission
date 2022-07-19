# CP template Version 1.006
# import io
import os
import sys
#import string
#from functools import cmp_to_key
#import itertools
#from itertools import combinations
#import collections
#from collections import deque
#from collections import Counter, defaultdict as dd
#import math
#from math import log, log2, ceil, floor, gcd, sqrt
#from heapq import heappush, heappop
#import bisect
#from bisect import insort_left as il
DEBUG = False

def main(f=None):
    init(f)
    #sys.setrecursionlimit(10**4)
    # ######## INPUT AREA BEGIN ##########            

    N, D = map(int, input().split())
    h = 2**(len(format(N-1, 'b')))
    tree = [-int(1e9)] * 2*h
    for i, e in enumerate(map(int, input().split()), h):
        res = 0
        l, r = max(h, i-D), i
        while l <= r:
            if l % 2:
                res = max(res, tree[l])
                l += 1
            if not r % 2:
                res = max(res, tree[r])
                r -= 1
            l //= 2
            r //= 2
        res += e

        tree[i] = res
        while i > 1:
            i //= 2
            tree[i] = max(tree[i*2], tree[i*2+1])

    return tree[1]

# TEMPLATE ###############################


enu = enumerate


def For(*args):
    return itertools.product(*map(range, args))


def Mat(h, w, default=None):
    return [[default for _ in range(w)] for _ in range(h)]


def nDim(*args, default=None):
    if len(args) == 1:
        return [default for _ in range(args[0])]
    else:
        return [nDim(*args[1:], default=default) for _ in range(args[0])]


def setStdin(f):
    global DEBUG, input
    DEBUG = True
    sys.stdin = open(f)
    input = sys.stdin.readline


def init(f=None):
    global input
    input = sys.stdin.readline #io.BytesIO(os.read(0, os.fstat(0).st_size)).readline 
    if os.path.exists("o"):
        sys.stdout = open("o", "w")
    if f is not None:
        setStdin(f)
    else:
        if len(sys.argv) == 1:
            if os.path.isfile("in/i"):
                setStdin("in/i")
            elif os.path.isfile("i"):
                setStdin("i")
        elif len(sys.argv) == 2:
            setStdin(sys.argv[1])
        else:
            assert False, "Too many sys.argv: %d" % len(sys.argv)


def pr(*args):
    if DEBUG:
        print(*args)


def pfast(*args, end="\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)


def parr(arr):
    for i in arr:
        print(i)


if __name__ == "__main__":
    print(main())