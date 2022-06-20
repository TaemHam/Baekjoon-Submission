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
#from heapq import heappush, heapreplace
#import bisect
#from bisect import bisect_left as bl, bisect_right as br
DEBUG = False


def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    watercopy = lambda x: len([1 for d in dc if lnd[x+d]])

    N, M = map(int, input().split())
    L = N+1
    dy = (0, 0, -1, -1, -1, 0, 1, 1, 1)
    dx = (0, -1, -1, 0, 1, 1, 1, 0, -1)
    dc = (-1-L, 1-L, 1+L, -1+L)
    lnd = [0] * L*L
    cld = [N*L-L, N*L-L+1, N*L-L-L, N*L-L-L+1]
    for y in range(0, N*L, L):
        lnd[y:y+N] = map(int, input().split())

    for _ in range(M):
        dir, spd = map(int, input().split())

        '''구름 이동 페이즈'''
        prv = set()
        loc = []
        for cur in cld:
            y, x = divmod(cur, L)
            nxt = (y+dy[dir]*spd)%N*L + (x+dx[dir]*spd)%N
            loc.append(nxt)
            lnd[nxt] += 1
            prv.add(nxt)

        '''복제 마법 페이즈'''
        for nxt in loc:
            lnd[nxt] += watercopy(nxt)

        '''구름 생성 페이즈'''
        cld = []
        for y in range(0, N*L, L):
            for xy in range(y, y+N):
                if lnd[xy] > 1 and xy not in prv:
                    lnd[xy] -= 2
                    cld.append(xy)

    print(sum(lnd))

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