# CP template Version 1.006
#import io
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
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

    def udt(g, i, v):
        while i <= len(g):
            g[i] += v
            i += i & -i

    def rng_udt(l, r, v):
        udt(dgrp, l, v)
        udt(dgrp, r+1, -v)
        udt(cgrp, l, (1-l)*v)
        udt(cgrp, r+1, r*v)

    def qry(g, i):
        t = 0
        while i:
            t += g[i]
            i -= i & -i
        return t

    N, M, K = map(int, input().split())
    ans = []
    cgrp = [0] * (10**6+10)
    dgrp = [0] * (10**6+10)

    for i in range(1, N+1):
        rng_udt(i, i, int(input().strip()))

    for _ in range(M+K):
        cmd = list(map(int, input().split()))
        if cmd[0] == 1:
            rng_udt(*cmd[1:])
        else:
            ans.append(str(qry(dgrp, cmd[2])*cmd[2] + qry(cgrp, cmd[2]) - qry(dgrp, cmd[1]-1)*(cmd[1]-1) - qry(cgrp, cmd[1]-1)))
    
    return '\n'.join(ans)

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