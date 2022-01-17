# CP template Version 1.006
import os
import sys
#import string
#from bshpctools import cmp_to_key, reduce, partial
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

    
    n = int(input().strip())

    grp = []
    blk = []
    wht = []
    clr = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            clr[i][j] = (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0)

    for i in range(n):
        grp.append(list(map(int, input().split())))
        for j in range(n):
            if grp[i][j] == 1 and clr[i][j] == 1:
                blk.append((i, j))
            if grp[i][j] == 1 and clr[i][j] == 0:
                wht.append((i, j))

    global Bcnt, Wcnt
    Bcnt, Wcnt = 0, 0

    u1 = [0] * (n * 2 - 1)
    u2 = [0] * (n * 2 - 1)


    def bshp(bishop, index, count):
        global Bcnt, Wcnt
        if index == len(bishop):
            rx, ry = bishop[index - 1]
            if clr[rx][ry]:
                Bcnt = max(Bcnt, count)
            else:
                Wcnt = max(Wcnt, count)
            return

        x, y = bishop[index]
        if u1[x + y] or u2[x - y + n - 1]:
            bshp(bishop, index + 1, count)
        else:
            u1[x + y] = 1
            u2[x - y + n - 1] = 1
            bshp(bishop, index + 1, count + 1)
            u1[x + y] = 0
            u2[x - y + n - 1] = 0
            bshp(bishop, index + 1, count)

    if len(blk) > 0:
        bshp(blk, 0, 0)
    if len(wht) > 0:
        bshp(wht, 0, 0)
    print(Bcnt + Wcnt)



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