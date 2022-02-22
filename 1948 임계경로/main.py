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

    N = int(input().strip())
    M = int(input().strip())
    grp_forw = [[] for _ in range(N+1)]
    grp_bakw = [[] for _ in range(N+1)]
    ind = [0] * (N+1)
    for _ in range(M):
        U, V, P = map(int, input().split())
        grp_forw[U].append((V, P))
        grp_bakw[V].append((U, P))
        ind[V] += 1
    S, D = map(int, input().split())
    dp = [0] * (N+1)
    q = [(0, S)]
    while q:
        d, p = q.pop()
        for np, td in grp_forw[p]:
            ind[np] -= 1
            dp[np] = max(dp[np], d + td)
            if ind[np]:
                continue
            q.append((dp[np], np))
    
    q = [(dp[D], D)]
    vis = [0] * (N+1)
    vis[D] = 1
    cnt = 0

    while q:
        d, p = q.pop()
        for np, td in grp_bakw[p]:
            nd = d - td
            if nd == dp[np]:
                cnt += 1
                if not vis[np]:
                    vis[np] = 1
                    q.append((nd, np))

    print(dp[D])
    print(cnt)

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