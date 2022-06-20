# CP template Version 1.006
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
#from itertools import product
from itertools import combinations
#import collections
#from collections import deque
#from collections import Counter, defaultdict as dd
#import math
#from math import log, log2, ceil, floor, gcd, sqrt
#from heapq import heappush, heappop
#import bisect
#from bisect import bisect_left as bl
DEBUG = False

def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########
    
    def add_to_air(x):
        air[x] = 1
        cnt.append(x)

    def add_to_wall(x):
        wll[x] = inf

    N, M = map(int, input().split())
    L = N+1
    mov = (1, -1, L, -L)
    inf = 2500
    cnt = []
    vir = []
    air = [0] * N*L
    wll = [0] * N*L + [inf] * L
    fnc = (add_to_air, add_to_wall, vir.append)

    for y in range(0, N*L, L):
        wll[y+N] = inf
        for x, e in enumerate(map(int, input().split())):
            fnc[e](y+x)

    if len(cnt):
        v = 0
        ans = inf
        for cque in combinations(vir, M):
            cque = list(cque)
            v += 1

            for cur in cque:
                wll[cur] = v
            c = len(cnt)

            for time in range(1, inf):
                nque = []

                for cur in cque:

                    for d in mov:

                        if wll[cur+d] < v:
                            wll[cur+d] = v
                            nque.append(cur+d)

                            if air[cur+d]:
                                c -= 1
                                if not c:
                                    ans = min(ans, time)
                                    nque = []
                                    cque.clear()
                                    break
                                
                if not nque:
                    break
                cque = nque
    else:
        ans = 0

    print(-1 if ans == inf else ans)

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