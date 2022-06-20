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
#from heapq import heappush, heappop
#import bisect
#from bisect import bisect_left as bl, bisect_right as br
DEBUG = False


def main(f=None):
    init(f)
    sys.setrecursionlimit(10003)
    # ######## INPUT AREA BEGIN ##########

    def dfs(p, n, k):
        l, r = grp[p]

        if l != -1:
            k = dfs(l, n+1, k)

        while len(brd) <= n:
            brd.append([])
        
        brd[n].append(k)
        k += 1
        
        if r != -1:
            k = dfs(r, n+1, k)
        
        return k
        
    N = int(input().strip())
    grp = [[] for _ in range(N+1)]
    brd = [[]]
    ind = set(range(1, N+1))
    for _ in range(N):
        p, l, r = map(int, input().split())
        ind.discard(l)
        ind.discard(r)
        grp[p] = (l, r)
    
    dfs(ind.pop(), 1, 1)

    dpt, max_wdt = 1, 1
    for i in range(2, len(brd)):
        wdt = brd[i][-1] - brd[i][0] + 1
        if wdt > max_wdt:
            dpt, max_wdt = i, wdt

    print(dpt, max_wdt)

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