# CP template Version 1.006
import os
import sys
from copy import deepcopy
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
#from itertools import product
#import collections
#from collections import deque
#from collections import Counter, defaultdict as dd
#import math
#from math import log, log2, ceil, floor, gcd, sqrt
#from heapq import heappush, heappop
#import bisect
#from bisect import bisect_left as bl, bisect_right as br
DEBUG = False


def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########
    global ans
    inf = int(1e9)
    arr = []
    ans = inf

    for _ in range(10):
        t = input().strip()
        v = 0
        for i in range(10):
            if t[i] == 'O':
                v = v | (1<<i)
        arr.append(v)

    dy = [1, -1, 0, 0, 0]
    dx = [0, 0, 0, 1, -1]

    def press(y, x, g, c):
        c += 1
        for i in range(5):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < 10 and 0 <= nx < 10:
                g[ny] = g[ny] ^ (1<<nx)
        return g, c

    
    def solve(g, c):
        global ans
        for y in range(1, 10):
            for x in range(10):
                if g[y-1] & (1 << x):
                    g, c = press(y, x, g, c)
        else:
            if g[9] == 0:
                ans = min(ans, c)


    def ini(grp, cnt, p):
        n_grp = deepcopy(grp)
        n_grp, n_cnt = press(0, p, n_grp, cnt)
        p += 1
        if p < 10:
            ini(grp, cnt, p)
            ini(n_grp, n_cnt, p)
        else:  
            solve(grp, cnt)
            solve(n_grp, n_cnt)

    ini(arr, 0, 0)
    print(ans if ans != inf else -1)



    # ######## INPUT AREA END ############


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
    input = sys.stdin.readline  # io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
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
    main()