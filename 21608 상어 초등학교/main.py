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

    N = int(input().strip())
    L = N+1
    scr = (0, 1, 10, 100, 1000)
    dir = (-1, 1, -L, L)
    ans = 0
    emp = [4] * L*L
    fnd = [0] * (N*N+1)
    sit = [-1] * (N*N+1)
    cls = [0] * L*N + [-1] * N
    chk = set(xy for y in range(0, L*N, L) for xy in range(y, y+N))
    for i in range(N):
        cls[i*L+N] = -1
        emp[i] -= 1
        emp[i+L*(N-1)] -= 1
        emp[i*L] -= 1
        emp[i*L+N-1] -= 1
    
    stdt, *frnd = map(int, input().split())
    fnd[stdt] = set(frnd)
    chk.discard(L+1)
    cls[L+1] = stdt
    sit[stdt] = L+1
    for d in dir:
        emp[L+1+d] -= 1

    for _ in range(1, N*N):
        stdt, *frnd = map(int, input().split())
        fnd[stdt] = set(frnd)
        
        fav = [0] * L*N
        cnd = []
        cur = 0
        for f in frnd:
            if sit[f] != -1:
                for d in dir:
                    if not cls[sit[f]+d]:
                        fav[sit[f]+d] += 1
                        if fav[sit[f]+d] > cur:
                            cur = fav[sit[f]+d]
                            cnd = [sit[f]+d]
                        elif fav[sit[f]+d] == cur:
                            cnd.append(sit[f]+d)
        if cnd:
            seat = max(cnd, key= lambda x: (emp[x], -x))
        else:
            seat = max(chk, key= lambda x: emp[x])

        chk.discard(seat)
        cls[seat] = stdt
        sit[stdt] = seat
        for d in dir:
            emp[seat+d] -= 1
    
    for stdt in range(1, len(sit)):
        ans += scr[len(set(cls[sit[stdt]+d] for d in dir) & fnd[stdt])]
    
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