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

    N = int(input().strip())
    INF = 1e9
    xcrd, ycrd = [], []
    for _ in range(N):
        x, y = map(int, input().split())
        xcrd.append(x)
        ycrd.append(y)
    dst = [[INF] * N for _ in range(N)]
    for i in range(N-1):
        for j in range(i+1, N):
            dst[i][j] = dst[j][i] = ((xcrd[i]-xcrd[j])**2 + (ycrd[i]-ycrd[j])**2)**(0.5)
    
    bit = [[INF] * (1<<N) for _ in range(N)]
    bit[0][1] = 0

    que = [(0, 1)]
    for cur, vis in que:
        for nxt in range(N):
            if not vis&(1<<nxt):
                if bit[nxt][vis|(1<<nxt)] == INF:
                    que.append((nxt, vis|(1<<nxt)))
                bit[nxt][vis|(1<<nxt)] = min(bit[nxt][vis|(1<<nxt)], bit[cur][vis] + dst[cur][nxt])
    
    res = []
    for i in range(1, N):
        res.append(bit[i][-1] + dst[i][0])

    return min(res)
    
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
    input = sys.stdin.readline # io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
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