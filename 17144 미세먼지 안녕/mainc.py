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

    r, c, t= map(int,input().split())
    puri = []
    grp1 = []
    for i in range(r):
        a = (list(map(int,input().split())))
        grp1.append(a)
        if a[0] == -1:
            puri.append((i, 0))

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    dy2 = [1, 0, -1, 0]
    dx2 = [0, 1, 0, -1]

    for tt in range(t):
        grp2 = [[0]*c for _ in range(r)]
        for y in range(r):
            for x in range(c):
                if grp1[y][x] >= 5:
                    dir = []
                    for i in range(4):
                        ny = y + dy[i]
                        nx = x + dx[i]
                        if 0 <= ny < r and 0 <= nx < c and grp1[ny][nx] != -1:
                            dir.append((ny, nx))
                    for ny, nx in dir:
                        grp2[ny][nx] += grp1[y][x] // 5
                    grp2[y][x] -= grp1[y][x] // 5 * len(dir)
        
        for y in range(r):
            for x in range(c):
                grp1[y][x] += grp2[y][x]
        

        for i in range(2):
            if i == 0:
                ddy = dy
                ddx = dx
                y_t = 0
                y_b = puri[i][0]
            else:
                ddy = dy2
                ddx = dx2
                y_t = puri[i][0]
                y_b = r-1

            y, x = puri[i]
            ny = y + ddy[0]
            nx = x + ddx[0]
            d = 0

            while (ny, nx) != puri[i]:
                grp1[y][x], grp1[ny][nx] = grp1[ny][nx], grp1[y][x]
                y, x = ny, nx
                ty = ny + ddy[d]
                tx = nx + ddx[d]
                if ty < y_t or ty > y_b or tx < 0 or tx >= c:
                    d += 1
                    ty = ny + ddy[d]
                    tx = nx + ddx[d]
                ny, nx = ty, tx

            grp1[y][x], grp1[ny][nx] = 0, grp1[y][x]

    ans = 0
    for i in grp1:
        ans += sum(i)
    print(ans+2)

    print(*grp1, sep='\n')

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