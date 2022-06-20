# CP template Version 1.006
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
#from bisect import bisect_left as bl
DEBUG = False

def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    def copy(mat, crd):
        for loc in cpy:
            mat[crd+loc] = 1

    R, C = map(int, input().split())
    L = C+1
    vis = [0] * R*L + [1] * L
    tgt = [0] * (R+1)*L
    lft = rgt = dwn = 0
    mov = (-1, 1, -L, L)
    dir = 'LRUD'
    ans = '-1'
    ttl = -1
    cpy = []
    bar = []
    for y in range(0, R*L, L):
        vis[y+C] = 1
        for xy, e in enumerate(input().strip(), y):
            if e == '.':
                continue

            elif e == 'T':
                if ttl == -1:
                    ttl = xy
                    vis[xy] = 2
                else:
                    cpy.append(ttl - xy)
                    lft = min(lft, xy%L - ttl%L)
                    rgt = max(rgt, xy%L - ttl%L)
                    dwn = max(dwn, xy//L - ttl//L)

            elif e == 'H':
                hom = xy
                tgt[xy] = 1

            else:
                bar.append(xy)
                vis[xy] = 1

    vis[C-rgt:R*L:L] = [1] * R
    vis[(R-dwn)*L:(R-dwn+1)*L] = [1] * L
    if lft:
        lft = abs(lft)-1
        vis[lft:R*L:L] = [1] * R
    
    copy(tgt, hom)
    for crd in bar:
        copy(vis, crd)

    for y in range(0, (R+1)*L, L):
        print(tgt[y:y+L])

    cque = [(ttl, '')]
    while True:
        nque = []
        for cur, rut in cque:

            if tgt[cur]:
                ans = rut
                nque = []
                break

            for d in range(4):
                if not vis[cur+mov[d]]:
                    vis[cur+mov[d]] = 1
                    nque.append((cur+mov[d], rut+dir[d]))

        if not nque:
            break
        cque = nque
    
    print(ans)

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