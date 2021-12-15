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

    input = sys.stdin.readline
    h,w = map(int,input().split())
    lake = []
    for _ in range(h):
        lake.append(list(input().strip()))
    water = set(['.', 'L'])

    swan_pos = []
    for x in range(w):
        for y in range(h):
            if lake[y][x] == 'L':
                swan_pos.append((x,y))

    dx = [0,-1,1,0]
    dy = [-1,0,0,1]

    def melt_bfs(q,v,melt_q):

        while q:
            x,y = q.popleft()
            v.add((x,y))

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < w and 0 <= ny < h and (nx,ny) not in v:
                    if lake[ny][nx] in water:
                        q.append((nx,ny))
                    elif lake[ny][nx] == 'X':
                            lake[ny][nx] = '.'
                            melt_q.append((nx,ny))
                            v.add((nx,ny))

        return melt_q


    def swan_bfs(q,swan_v,swan_q):

        while q:
            x,y = q.popleft()
            swan_v.add((x,y))

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < w and 0 <= ny < h and (nx,ny) not in swan_v:
                    if lake[ny][nx] in water:
                        q.append((nx,ny))
                    elif lake[ny][nx] == 'X':
                        swan_q.append((nx,ny))
                    if (nx,ny) == swan_pos[1]:
                        print(day)
                        return []

        return swan_q


    swan_v = set()
    day = 0
    swan_q = swan_bfs(deque([swan_pos[0]]),swan_v,deque())

    q = deque()
    v = set()
    melt_q = deque()
    for x in range(w):
        for y in range(h):
            if lake[y][x] in water and (x,y) not in v:
                q.append((x,y))
                melt_q = melt_q + melt_bfs(q,v,deque())
    while True:
        day += 1
        swan_q = swan_bfs(swan_q,swan_v,deque())
        if len(swan_q) == 0:
            break
        melt_q = melt_bfs(melt_q,v,deque())

    



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