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

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    dd = [1, 0, 3, 2]
    R, C, M = map(int, input().split())

    g = [[0] * C for i in range(R)]
    for i in range(1, M + 1):
        r, c, s, d, z = map(int, input().split())
        g[r-1][c-1] = [s, d-1, z]

    def move():
        t = [[0] * C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if g[i][j] != 0:
                    x, y, s, d, z = i, j, g[i][j][0], g[i][j][1], g[i][j][2]
                    while s > 0:
                        x += dx[d]
                        y += dy[d]
                        if 0 <= x < R and 0 <= y < C:
                            s -= 1
                        else:
                            x -= dx[d]
                            y -= dy[d]
                            d = dd[d]
                    if t[x][y] == 0:
                        t[x][y] = [g[i][j][0], d, z]
                    else:
                        if t[x][y][2] < z:
                            t[x][y] = [g[i][j][0], d, z]
        return t

    ans = 0
    for i in range(C):
        for j in range(R):
            if g[j][i] != 0:
                ans += g[j][i][2]
                g[j][i] = 0
                break
        g = move()
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