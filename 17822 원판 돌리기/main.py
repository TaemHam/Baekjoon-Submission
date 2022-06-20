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

    N, M, T = map(int, input().split())
    dir = ((1, 0), (0, 1))
    grp = []
    ttl = 0
    for i in range(N):
        grp.append(list(map(int, input().split())))
        ttl += sum(grp[i])
    cnt = N * M

    for _ in range(T):
        
        X, D, K = map(int, input().split())
        stk = set()

        for i in range(X-1, N, X):
            if D:
                grp[i] = grp[i][K:] + grp[i][:K]
            else:
                grp[i] = grp[i][-K:] + grp[i][:-K]

        for y in range(N):
            for x in range(M):
                if grp[y][x]:
                    for dy, dx in dir:
                        ny = y + dy
                        nx = (x + dx) % M
                        if ny < N and grp[y][x] == grp[ny][nx]:
                            stk.add((y, x))
                            stk.add((ny, nx))
        
        if stk:
            for y, x in stk:
                ttl -= grp[y][x]
                cnt -= 1
                grp[y][x] = 0
            if not cnt:
                break
        else:
            avg = ttl/cnt
            for y in range(N):
                for x in range(M):
                    if grp[y][x]:
                        if grp[y][x] < avg:
                            grp[y][x] += 1
                            ttl += 1
                        elif grp[y][x] > avg:
                            grp[y][x] -= 1
                            ttl -= 1
                            
    print(ttl)

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