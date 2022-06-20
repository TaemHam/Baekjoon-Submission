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

    R, C = map(int, input().split())
    ans = 0
    num = lambda y, x: 1 << ord(grp[y][x])-65
    vis = [[0] * C for _ in range(R)]
    grp = [input().strip() for _ in range(R)]
    oob = [[1] * (C+1) for _ in range(R)] + [[0] * (C+1)]
    for i in range(R):
        oob[i][C] = 0
    dy = (1, -1, 0, 0)
    dx = (0, 0, 1, -1)
    q = [(0, 0, 1, num(0, 0))]

    while q:
        y, x, cnt, cur = q.pop()
        if ans < cnt:
            ans = cnt
            if ans == 26:
                break
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if oob[ny][nx] and not cur & num(ny, nx) and vis[ny][nx] ^ (cur|num(ny, nx)):
                vis[ny][nx] = cur|num(ny, nx)
                q.append((ny, nx, cnt+1, cur|num(ny, nx)))

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