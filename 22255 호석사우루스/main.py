# CP template Version 1.006
#import io
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
#from itertools import combinations
#import collections
#from collections import deque
#from collections import Counter, defaultdict as dd
#import math
#from math import log, log2, ceil, floor, gcd, sqrt
from heapq import heappush, heappop
#import bisect
#from bisect import insort_left as il
DEBUG = False

def main(f=None):
    init(f)
    #sys.setrecursionlimit(10**4)
    # ######## INPUT AREA BEGIN ##########
    N, M = map(int, input().split())
    SR, SC, ER, EC = map(lambda x: int(x)-1, input().split())
    L = M+1
    vis = [[int(1e9)] * N*L for _ in range(3)]
    mov = ((L, -L, 1, -1), (L, -L), (1, -1))
    brd = [-1] * (N+1)*L
    tgt = ER * L + EC
    ans = -1

    for y in range(0, N*L, L):
        brd[y:y+M] = map(int, input().split())


    vis[0][SR * L + SC] = 0
    heap = [(0, SR * L + SC, 0)]
    while heap:
        imp, cur, day = heappop(heap)

        if imp > vis[day][cur]:
            continue

        if cur == tgt:
            ans = imp
            break

        day = (day+1)%3
        for d in mov[day]:
            if brd[cur+d] != -1 and imp + brd[cur+d] < vis[day][cur+d]:
                vis[day][cur+d] = imp + brd[cur+d]
                heappush(heap, (vis[day][cur+d], cur+d, day))
        
    return ans

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