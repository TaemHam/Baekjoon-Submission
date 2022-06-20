# CP template Version 1.006
#import io
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
    # ######## INPUT AREA BEGIN ##########

    ans = []

    for _ in range(int(input().strip())):
        N, M, T = map(int, input().split())
        S, G, H = map(int, input().split())
        tgt = set([G, H])
        dst = [int(1e9)] * (N+1)
        dst[S] = 0
        tbl = [0] * (N+1)
        que = [(0, S, 0)]
        grp = [[] for _ in range(N+1)]
        for _ in range(M):
            A, B, D = map(int, input().split())
            grp[A].append((D, B))
            grp[B].append((D, A))
            
        while que:
            d, p, flg = heappop(que)
            if dst[p] < d:
                continue

            for td, np in grp[p]:
                nd = td + d
                if nd < dst[np] or (nd == dst[np] and not tbl[np]):
                    if flg or (p in tgt and np in tgt):
                        tbl[np] = 1
                        heappush(que, (nd, np, 1))
                    elif nd < dst[np]:
                        tbl[np] = 0
                        heappush(que, (nd, np, 0))
                    dst[np] = nd

        res = []
        for _ in range(T):
            E = int(input().strip())
            if tbl[E]:
                res.append(E)
    
        ans.append(' '.join(map(str, sorted(res))))
    
    print('\n'.join(ans))

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
    input = sys.stdin.readline #io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
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