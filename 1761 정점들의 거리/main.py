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

    n = int(input().strip())
    grp = [[] for _ in range(n+1)]
    par = [[0] * (n+1)]
    dst = [0] * (n+1)
    dep = [0] * (n+1)
    dep[1] = 1
    q = [1]

    for _ in range(n-1):
        a, b, c = map(int, input().split())
        grp[a].append((b, c))
        grp[b].append((a, c))
    
    while q:
        p = q.pop()
        for i, c in grp[p]:
            if not dep[i]:
                par[0][i] = p
                dst[i] = dst[p] + c
                dep[i] = dep[p] + 1
                q.append(i)

    max_dep = len(format(max(dep), 'b')) - 1

    for i in range(1, max_dep+1):
        tmp = [0] * (n+1)
        for j in range(1, n+1):
            tmp[j] = par[i-1][par[i-1][j]]
        par.append(tmp)
    
    for _ in range(int(input().strip())):

        a, b = map(int, input().split())
        ao, bo = a, b
        if dep[a] > dep[b]:
            a, b = b, a
        
        for i in range(max_dep, -1, -1):
            if dep[b] - dep[a] >= 2**i:
                b = par[i][b]
        
        if a != b:
            for i in range(max_dep, -1, -1):
                if par[i][a] != par[i][b]:
                    a = par[i][a]
                    b = par[i][b]
            a = par[0][a]
        
        print(dst[ao] + dst[bo] - 2*dst[a])

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