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

    n, m = map(int, input().split())
    chs = set()
    for y in range(n):
        l = input().split()
        for x in range(m):
            if l[x] == '1':
                chs.add((y, x))
    dy = [1, -1, 0 ,0]
    dx = [0, 0, 1, -1]
    air = set()
    time = 0

    def is_air(q):
        while q:
            ay, ax = q.pop()
            air.add((ay, ax))
            for i in range(4):
                nay = ay + dy[i]
                nax = ax + dx[i]
                if 0<=nay<n and 0<=nax<m and (nay, nax) not in air and (nay, nax) not in chs:
                    air.add((nay, nax))
                    q.append((nay, nax))
    
    def is_melt(time):
        n_chs = set()
        melted = []
        for y, x in chs:
            touch = 0
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if (ny, nx) in air:
                    touch += 1
            if touch < 2:
                n_chs.add((y, x))
            else:
                melted.append((y, x))
        time += 1
        return time, n_chs, melted
    
    is_air([(0, 0)])
    while chs:
        time, chs, melted = is_melt(time)
        if not melted:
            break
        is_air(melted)
    print(time)

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