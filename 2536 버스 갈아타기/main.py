# CP template Version 1.006
# import io
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
    # ######## INPUT AREA BEGIN ##########

    check = lambda r1, r2: r1[0] <= r2[1] and r2[0] <= r1[1]

    N, M = map(int, input().split())
    K = int(input().strip())
    h = v = 0
    hor = [[] for _ in range(N+1)]
    ver = [[] for _ in range(M+1)]
    grp = [[] for _ in range(K+1)]
    vis = [0] * (K+2)

    for _ in range(K):
        b, x1, y1, x2, y2 = map(int, input().split())
        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            h += y2 - y1
            arr, f, l, r = hor, x1, y1, y2
        else:
            if x1 > x2:
                x1, x2 = x2, x1
            v += x2 - x1
            arr, f, l, r = ver, y1, x1, x2

        for e in arr[f]:
            if check(e[1], (l, r)):
                grp[e[0]].append(b)
                grp[b].append(e[0])
        arr[f].append((b, (l, r)))
    
    ar1, ar2 = (hor, ver) if h <= v else (ver, hor)

    for ai in range(len(ar1)):
        for b1, (l, r) in ar1[ai]:
            for c2 in ar2[l:r+1]:
                for b2, r2 in c2:
                    if check(r2, (ai, ai)):
                        grp[b1].append(b2)
                        grp[b2].append(b1)

    sx, sy, dx, dy = map(int, input().split())

    for b, r in hor[sx]:
        if check(r, (sy, sy)):
            grp[0].append(b)
    for b, r in ver[sy]:
        if check(r, (sx, sx)):
            grp[0].append(b)
    for b, r in hor[dx]:
        if check(r, (dy, dy)):
            grp[b].append(K+1)
    for b, r in ver[dy]:
        if check(r, (dx, dx)):
            grp[b].append(K+1)

    cque = [0]
    vis[0] = 1
    for trns in range(-1, K+2):
        nque = []
        for cur in cque:
            if cur == K+1:
                nque = []
                break
            for nxt in grp[cur]:
                if not vis[nxt]:
                    vis[nxt] = 1
                    nque.append(nxt)
        if not nque:
            break
        cque = nque
    
    return trns

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
    input = sys.stdin.readline # io.BytesIO(os.read(0, os.fstat(0).st_size)).readline 
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