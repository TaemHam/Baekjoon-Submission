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

    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    n, m = map(int, input().split())
    brd = [list(map(int, input().split()))]
    arr = set()
    cnt = 0
    for y in range(1, n-1):
        t = list(map(int, input().split()))
        for x in range(1, m-1):
            if t[x] != 0:
                arr.add((y, x))
        brd.append(t)
    
    brd.append(list(map(int, input().split())))
    
    while True:
        a, b = len(arr), 0
        if a == 0:
            print(0)
            break
        q = [arr.pop()]
        arr.add(q[0])
        vis = [[-1] * m for _ in range(n)]
        while q:
            y, x = q.pop()
            if vis[y][x] != -1:
                continue
            vis[y][x] = 0
            b += 1
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if brd[ny][nx] == 0:
                    vis[y][x] += 1
                else:
                    q.append((ny, nx))

        if a != b:
            print(cnt)
            break
        
        t = set()
        for y, x in arr:
            brd[y][x] -= vis[y][x]
            if brd[y][x] <= 0:
                brd[y][x] = 0
                t.add((y, x))
        arr -= t

        cnt += 1

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