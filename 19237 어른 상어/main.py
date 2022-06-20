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

    N, M, K = map(int, input().split())
    L = N+1
    M += 1
    mov = (-L, L, -1, 1)
    pri = [[] for _ in range(M)]
    rmn = set(range(1, M))
    loc = [0] * M
    brd = [0] * N*L
    odr = [0] * N*L + [-1] * L
    who = [0] * L*L
    ans = -1
    for y in range(0, N*L, L):
        odr[y+N] = -1
        brd[y:y+N] = map(int, input().split())
        for xy in range(y, y+N):
            if brd[xy]:
                loc[brd[xy]] = xy
                odr[xy] = K
                who[xy] = brd[xy]
    
    dir = [0] + list(map(lambda x: int(x)-1, input().split()))
    for i in range(1, M):
        for _ in range(4):
            pri[i].append(tuple(map(lambda x: int(x)-1, input().split())))

    for time in range(1, 1001):

        '''이동 페이즈'''
        for shk in rmn:
            brd[loc[shk]] = 0
            cnd = ()

            for i in range(4):
                nd = pri[shk][dir[shk]][i]
                nxt = loc[shk] + mov[nd]
                if not odr[nxt]:
                    cnd = (nxt, nd)
                    break
                elif who[nxt] == shk and not cnd:
                    cnd = (nxt, nd)
            
            loc[shk], dir[shk] = cnd

        '''냄새 페이즈'''
        for y in range(0, N*L, L):
            for xy in range(y, y+N):
                if odr[xy]:
                    odr[xy] -= 1

        '''도망 페이즈'''
        run = set()
        for shk in rmn:
            cur = loc[shk]
            if not brd[cur]:
                brd[cur] = shk
                who[cur] = shk
                odr[cur] = K
            else:
                run.add(shk)
        rmn -= run

        '''정답 체크 페이즈'''
        if len(rmn) == 1:
            ans = time
            break
    
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