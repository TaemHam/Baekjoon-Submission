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
from heapq import heappush, heappop
#import bisect
#from bisect import bisect_left as bl, bisect_right as br
DEBUG = False


def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    inf = int(1e9)
    n, m, x = map(int, input().split())
    go_grp = [[] for _ in range(n+1)]
    cm_grp = [[] for _ in range(n+1)]

    for _ in range(m):
        s, e, t = map(int, input().split())
        go_grp[e].append((t, s))
        cm_grp[s].append((t, e))
    go_tbl = [inf] * (n+1)
    cm_tbl = [inf] * (n+1)
    go_tbl[x] = 0
    cm_tbl[x] = 0
    gq = [(0, x)]
    cq = [(0, x)]

    while gq:
        d, p = heappop(gq)
        if go_tbl[p] > d:
            continue
        for nd, np in go_grp[p]:
            td = d + nd
            if td < go_tbl[np]:
                go_tbl[np] = td
                heappush(gq, (td, np))
    
    while cq:
        d, p = heappop(cq)
        if cm_tbl[p] < d:
            continue
        for nd, np in cm_grp[p]:
            td = d + nd
            if td < cm_tbl[np]:
                cm_tbl[np] = td
                heappush(cq, (td, np))
    
    ans = 0
    for i in range(1, n+1):
        ans = max(go_tbl[i] + cm_tbl[i], ans)
    
    print(ans)

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
    input = sys.stdin.readline  # by default
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