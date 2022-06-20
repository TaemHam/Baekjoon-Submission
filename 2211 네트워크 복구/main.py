# CP template Version 1.006
#import io
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
#from bisect import insort_left as il
DEBUG = False


def main(f=None):
    init(f)
    # ######## INPUT AREA BEGIN ##########

    V, E = map(int, input().split())
    V += 1
    grp = [[] for _ in range(V)]
    tbl = [0] * V
    dst = [int(1e9)] * V
    dst[1] = 0
    que = [(0, 1)]
    ans = []

    for _ in range(E):
        A, B, C = map(int, input().split())
        grp[A].append((C, B))
        grp[B].append((C, A))
    
    while que:
        d, p = heappop(que)
        for td, np in grp[p]:
            nd = d + td
            if dst[np] > nd:
                tbl[np] = p
                dst[np] = nd
                heappush(que, (nd, np))
    
    for i in range(2, V):
        ans.append((f'{i} {tbl[i]}'))

    print(f'{V-2}\n'+'\n'.join(ans))

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
    main()