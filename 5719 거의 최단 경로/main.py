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

    INF = int(1e9)
    while True:
        N, M = map(int, input().split())
        if N == 0 and M == 0:
            break

        S, D = map(int, input().split())

        grp = [[0] * N for _ in range(N)]
        for _ in range(M):
            U, V, P = map(int, input().split())
            grp[U][V] = P

        dp_p = [INF] * N
        dp_r = [set() for _ in range(N)]
        dp_p[S] = 0
        q = [(0, S)]
        
        
        while q:
            d, p = heappop(q)
            if dp_p[p] < d:
                continue
            for np in range(N):
                if not grp[p][np]:
                    continue

                nd = d + grp[p][np]
                if nd < dp_p[np]:
                    dp_r[np] = dp_r[p].union([(p, np)])
                    dp_p[np] = nd
                    heappush(q, (nd, np))
                elif nd == dp_p[np]:
                    dp_r[np] = dp_r[p].union(dp_r[np])
                    dp_r[np].add((p, np))

        for i in dp_r[D]:
            grp[i[0]][i[1]] = 0

        dp_p = [INF] * N
        dp_p[S] = 0
        q = [(0, S)]

        while q:
            d, p = heappop(q)
            if dp_p[p] < d:
                continue
            for np in range(N):
                if not grp[p][np]:
                    continue
                nd = d + grp[p][np]

                if nd < dp_p[np]:
                    dp_p[np] = nd
                    heappush(q, (nd, np))

        ans = dp_p[D]
        print(ans if ans != INF else -1)

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