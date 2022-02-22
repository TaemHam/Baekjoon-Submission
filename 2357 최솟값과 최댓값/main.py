# CP template Version 1.006
import os
import sys
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

    def sgmt(stt, end, nde):
        if stt == end:
            grp[nde] = [arr[stt], arr[stt]]
            return grp[nde]

        mid = (stt+end) // 2
        l = sgmt(stt, mid, nde*2)
        r = sgmt(mid+1, end, nde*2+1)
        grp[nde] = [min(l[0], r[0]), max(l[1], r[1])]
        return grp[nde]
    
    def sfnd(stt, end, nde, L, R):
        if R < stt or end < L:
            return [inf, 0]
        if L <= stt and end <= R:
            return grp[nde]
        
        mid = (stt+end) // 2
        l = sfnd(stt, mid, nde*2, L, R)
        r = sfnd(mid+1, end, nde*2+1, L, R)
        return [min(l[0], r[0]), max(l[1], r[1])]

    n, m = map(int, input().split())
    inf = int(1e9)
    grp = [0] * (n*4)
    arr = [0] + [int(input().strip()) for _ in range(n)]
    sgmt(1, n, 1)

    for _ in range(m):
        a, b = map(int, input().split())
        print(*sfnd(1, n, 1, a, b))

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