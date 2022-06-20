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

    N, M, K = map(int, input().split())
    L = N+1
    grp = [[] for _ in range(L)]
    brd = [[int(1e10)]*L for _ in range(K+1)]
    que = [(0, K, 1)]
    brd[K][1] = 0

    for _ in range(M):
        s, e, t = map(int, input().split())
        grp[s].append((t, e))
        grp[e].append((t, s))

    while que:
        ttl, cnt, cur = heappop(que)

        if ttl > brd[cnt][cur]:
            continue

        if cnt:
            for nxt in grp[cur]:
                if brd[cnt-1][nxt[1]] > ttl:
                    brd[cnt-1][nxt[1]] = ttl
                    heappush(que, (ttl, cnt-1, nxt[1]))

        for dst, nxt in grp[cur]:
            if brd[cnt][nxt] > ttl+dst:
                brd[cnt][nxt] = ttl+dst
                heappush(que, (ttl+dst, cnt, nxt))
    
    print(min(i[N] for i in brd))

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