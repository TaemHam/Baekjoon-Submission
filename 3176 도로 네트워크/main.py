# CP template Version 1.006
#import io
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
#from heapq import heappush, heappop
#import bisect
#from bisect import bisect_left as bl, bisect_right as br
DEBUG = False

def main(f=None):
    init(f)
    #sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    N = int(input().strip()) + 1
    grp = [[] for _ in range(N)]
    par = [[0] * (N)]
    mxm = [[0] * (N)]
    mnm = [[int(1e6)] * (N)]
    dep = [0] * (N)
    dep[1] = 1
    que = [1]
    ans = []

    for _ in range(N-2):
        a, b, c = map(int, input().split())
        grp[a].append((b, c))
        grp[b].append((a, c))

    for p in que:
        for i, c in grp[p]:
            if not dep[i]:
                par[0][i] = p
                mxm[0][i] = mnm[0][i] = c
                dep[i] = dep[p] + 1
                que.append(i)

    max_dep = len(format(max(dep), 'b')) - 1

    for i in range(1, max_dep+1):
        tmp = [0] * (N)
        tmx = [0] * (N)
        tmn = [int(1e6)] * (N)
        for j in range(1, N):
            tmp[j] = par[i-1][par[i-1][j]]
            tmx[j] = max(mxm[i-1][j], mxm[i-1][par[i-1][j]])
            tmn[j] = min(mnm[i-1][j], mnm[i-1][par[i-1][j]])
        par.append(tmp)
        mxm.append(tmx)
        mnm.append(tmn)

    for _ in range(int(input().strip())):
        a, b = map(int, input().split())
        rmx, rmn = 0, int(1e6)
        
        if dep[a] > dep[b]:
            a, b = b, a
        
        for i in range(max_dep, -1, -1):
            if dep[b] - dep[a] >= 2**i:
                rmx, rmn = max(rmx, mxm[i][b]), min(rmn, mnm[i][b])
                b = par[i][b]
        if a != b:
            for i in range(max_dep, -1, -1):
                if par[i][a] != par[i][b]:
                    rmx, rmn = max(rmx, mxm[i][a], mxm[i][b]), min(rmn, mnm[i][a], mnm[i][b])
                    a = par[i][a]
                    b = par[i][b]
            rmx, rmn = max(rmx, mxm[0][a], mxm[0][b]), min(rmn, mnm[0][a], mnm[0][b])

        ans.append(f'{rmn} {rmx}')
    
    return '\n'.join(ans)

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
    print(main())
    