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
#from heapq import heappush, heapreplace
#import bisect
#from bisect import bisect_left as bl, bisect_right as br
DEBUG = False


def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    INF = int(1e9)
    N = int(input().strip())
    par = list(range(N+1))
    grp = [[INF] * (N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        grp[i][i] = 0

    for _ in range(int(input().strip())):
        a, b = map(int, input().split())
        grp[a][b] = 1
        grp[b][a] = 1

        while a != par[a]:
            a = par[a]
        while b != par[b]:
            b = par[b]
        
        if a > b:
            a, b = b, a
        
        par[b] = a
    
    for mid in range(1, N+1):
        for stt in range(1, N+1):
            for end in range(1, N+1):
                grp[stt][end] = min(grp[stt][end], grp[stt][mid] + grp[mid][end])

    ind = [0] * (N+1)
    for i in range(1, N+1):
        ind[i] = max(j if j != INF else 0 for j in grp[i])
    
    chk = dict()
    for i in range(1, N+1):
        o = i
        while o != par[o]:
            o = par[o]
        
        if o not in chk:
            chk[o] = i
        else:
            chk[o] = min(chk[o], i, key= lambda x: ind[x])
    
    print(str(len(chk)) + '\n' + '\n'.join(map(str, sorted(chk.values()))))
    
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