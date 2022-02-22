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

    def dfs_land(a, b):
        q = [(a, b)]
        brd[a][b] = num
        while q:
            y, x = q.pop()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0 <= nx < N:
                    if brd[ny][nx] == 1:
                        brd[ny][nx] = num
                        q.append((ny, nx))
                    elif not brd[ny][nx]:
                        brd[ny][nx] = num
                        dq.append((ny, nx))
                    elif brd[ny][nx] != num:
                        print(stp)
                        return 1

    N = int(input().strip())
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    dq = deque()
    cnd = set()
    num = 1
    stp = 1
    brd = [list(map(int, input().split())) for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if brd[y][x] == 1:
                num += 1
                if dfs_land(y, x):
                    return
    
    dq.append((-1, -1))

    while dq:
        y, x = dq.popleft()
        if y == -1:
            if cnd:
                break
            stp += 1
            dq.append((-1, -1))
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if brd[ny][nx] == brd[y][x]:
                    continue
                elif not brd[ny][nx]:
                    brd[ny][nx] = brd[y][x]
                    dq.append((ny, nx))
                else:
                    cnd.add((brd[y][x], brd[ny][nx]))
    
    for a, b in cnd:
        if a < b:
            ans = stp * 2
            break
        else:
            ans = stp * 2 + 1
            
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