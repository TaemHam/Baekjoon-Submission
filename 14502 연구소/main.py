# CP template Version 1.006
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
#from itertools import product
#import collections
from collections import deque
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

    inf = 65
    n, m = map(int, input().split())
    mat = []
    zloc = []
    vloc = []
    for y in range(n):
        t = list(input().split())
        for x in range(m):
            if t[x] == '0':
                zloc.append((y,x))
            elif t[x] == '2':
                vloc.append((y,x))
        mat.append(t)
    zcnt = len(zloc)
    min_vcnt= inf

    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    def spread_virus(min_v):
        vcnt = len(vloc)
        v = [[True] * m for _ in range(n)]
        q = deque(vloc)
        while q:
            y, x = q.popleft()
            v[y][x] = False
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0<=ny<n and 0<=nx<m and mat[ny][nx] == '0' and v[ny][nx] == True:
                    v[ny][nx] = False
                    q.append((ny, nx))
                    vcnt += 1
            if vcnt >= min_v:
                return inf
        return min(min_v, vcnt)


    for a in range(zcnt):
        ay, ax = zloc[a]
        mat[ay][ax] = '1'
        for b in range(a+1, zcnt):
            by, bx = zloc[b]
            mat[by][bx] = '1'
            for c in range(b+1, zcnt):
                cy, cx = zloc[c]
                mat[cy][cx] = '1'
                min_vcnt= min(spread_virus(min_vcnt), min_vcnt)
                mat[cy][cx] = '0'
            mat[by][bx] = '0'
        mat[ay][ax] = '0'
    
    print(zcnt - min_vcnt - 3 + len(vloc))


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
    input = sys.stdin.readline  # by default
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