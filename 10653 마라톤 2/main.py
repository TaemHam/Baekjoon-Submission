# CP template Version 1.006
#import io
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
#from itertools import permutations
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
    #sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    def min_dst(k, n):
        for idx in range(k+1):
            mmr[k][n] = min(mmr[k][n], mmr[k-idx][n-idx-1] + dst[n-idx-1][n])

    N, K = map(int, input().split())
    K = min(K, N-2) + 1
    grp = [tuple(map(int, input().split())) for _ in range(N)]

    dst = [[-1] * N for _ in range(N)]
    for i in range(N-1):
        for j in range(i+1, min(i+K+1, N)):
            dst[i][j] = abs(grp[i][0] - grp[j][0]) + abs(grp[i][1] - grp[j][1])

    mmr = [[int(1e9)] * N for _ in range(K)]
    mmr[0][0] = 0
    for i in range(K):
        for j in range(i+1, i+N-K):
            min_dst(i, j)
    print(*mmr, sep='\n')
    min_dst(K-1, N-1)

    return mmr[-1][-1]

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
    print(main())