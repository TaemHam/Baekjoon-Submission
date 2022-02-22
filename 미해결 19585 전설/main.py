# CP template Version 1.006
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
#from itertools import product
#import collections
#from collections import deque
from collections import defaultdict as dd
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

    n, m = map(int, input().split())
    clr_d = dd(int)
    for _ in range(n):
        clr = input().strip()
        p = 1
        while p < len(clr):
            tmp = clr[:p]
            if clr_d[tmp] == 2:
                clr_d[tmp] = 3
            else:
                clr_d[tmp] = 1
            p += 1
        else:
            clr_d[clr] = 2

    nck_d = dd(int)
    for _ in range(m):
        nck = input().strip()
        p = 1
        while p < len(nck):
            tmp = nck[:p]
            if nck_d[tmp] == 2:
                nck_d[tmp] = 3
            else:
                nck_d[tmp] = 1
            p += 1
        else:
            nck_d[nck] = 2

    tc = int(input().strip())
    for _ in range(tc):
        team = input().strip()
        p = 1
        flg = 0
        while p <= len(team):
            tmp = team[:p]
            if tmp in clr_d:
                p += 1
                if clr_d[tmp] == 1:
                    continue
                if clr_d[tmp] == 3:
                    t = p+1
                    if t < len(team) and team[:t] in clr_d:
                        continue
                flg = p-1
                break
            else:
                break

        if not flg:
            print('No')
            continue

        fin = 0

        while p <= len(team):
            tmp = team[flg:p]
            if tmp in nck_d:
                p += 1
                if nck_d[tmp] == 1:
                    continue
                if p <= len(team):
                    continue
                fin = 1
                break
            else:
                break
        if fin == 0:
            print('No')
        else:
            print('Yes')


    

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