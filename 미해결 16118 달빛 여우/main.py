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
from heapq import heappush, heappop
#import bisect
#from bisect import bisect_left as bl
DEBUG = False

def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    N, M = map(int, input().split())
    N += 1
    inf = int(1e9)
    grp = [[] for _ in range(N)]
    fox = [inf] * N
    wlf = [[inf] * N for _ in range(2)]
    fox[1] = wlf[0][1] = 0

    for _ in range(M):
        a, b, d = map(int, input().split())
        grp[a].append((b, d<<1))
        grp[b].append((a, d<<1))
    
    heap = [(0, 1, 0)]
    while heap:
        ttl, cur, flg = heappop(heap)

        if ttl > wlf[flg][cur]:
            continue

        for nxt, dst in grp[cur]:

            if flg:
                nttl = ttl + dst*2
            else:
                nttl = ttl + dst//2

            if nttl < wlf[1-flg][nxt]:
                wlf[1-flg][nxt] = nttl
                heappush(heap, (nttl, nxt, 1-flg))
    
    heap = [(0, 1)]
    while heap:
        ttl, cur = heappop(heap)

        if ttl > fox[cur]:
            continue

        for nxt, dst in grp[cur]:

            nttl = ttl + dst
            if nttl < fox[nxt]:
                fox[nxt] = nttl
                heappush(heap, (nttl, nxt))
    
    ans = 0
    for i in range(2, N):
        if fox[i] < min(wlf[0][i], wlf[1][i]):
            ans += 1

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