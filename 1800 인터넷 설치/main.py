# CP template Version 1.006
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
#from itertools import permutations
#import collections
#from collections import deque
#from collections import Counter, defaultdict as dd
#import math
#from math import log, log2, ceil, floor, gcd, sqrt
from heapq import heappush, heappop
#import bisect
#from bisect import bisect_left as bl, bisect_roloc[xyight as brloc[xy]
DEBUG = False

def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    def djk(x):
        vis = [int(1e9)] * (N+1)
        vis[1] = 0
        heap = [(0, 1)]
        while heap:
            cnt, cur = heappop(heap)
            if cnt > vis[cur]:
                continue
            for nxt, dst in grp[cur]:
                if dst > x:
                    if cnt+1 < vis[nxt]:
                        vis[nxt] = cnt+1
                        heappush(heap, (cnt+1, nxt))
                else:
                    if cnt < vis[nxt]:
                        vis[nxt] = cnt
                        heappush(heap, (cnt, nxt))

        return vis[N] <= K 

    N, P, K = map(int, input().split())
    grp = [[] for _ in range(N+1)]
    lft = rgt = 0
    ans = int(1e9)
    for _ in range(P):
        u, v, c = map(int, input().split())
        rgt = max(rgt, c)
        grp[u].append((v, c))
        grp[v].append((u, c))
    
    while lft <= rgt:
        mid = (lft+rgt)//2
        if djk(mid):
            ans = mid
            rgt = mid - 1
        else:
            lft = mid + 1

    return ans if ans != int(1e9) else -1

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
    print(main())
    