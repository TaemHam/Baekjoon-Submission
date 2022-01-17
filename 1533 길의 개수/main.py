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

    def mul(a, b):
        return [[sum(a[i][k] * b[k][j] for k in range(L)) % MOD for j in range(L)] for i in range(L)]

    N, S, E, T = map(int, input().split())
    L = 5*N
    S -= 1
    E -= 1
    MOD = 1000003

    grp = [[0] * (L) for _ in range(L)]
    grp_a = [[0] * (L) for _ in range(L)]
    for i in range(L):
        grp_a[i][i] = 1

    for y in range(N):
        for x in range(1, 5):
            grp[y*5+x][y*5+x-1] = 1
    
    for y in range(N):
        l = list(map(int, list(input().strip())))
        for x in range(N):
            if l[x] == 1:
                grp[y*5][x*5] = 1
            elif l[x] > 1:
                grp[y*5][x*5 + l[x]-1] = 1
    
    while T:
        if T % 2:
            grp_a = mul(grp_a, grp)
            T -= 1
        grp = mul(grp, grp)
        T //= 2
    

    print(grp_a[S*5][E*5])

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