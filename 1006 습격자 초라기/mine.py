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
    #sys.setrecursionlimit(10**5)
    # ######## INPUT AREA BEGIN ##########


    T = int(input().strip())

    for _ in range(T):
        N, W = map(int, input().split())
        E = [[] for _ in range(N)]
        for _ in range(2):
            t = list(map(int, input().split()))
            for i in range(N):
                E[i].append(t[i])
        if N == 1:
            print(1 if sum(E[0]) <= W else 2)
            continue
        
        dp = [[0] * 3 for _ in range(N+1)]
        d0 = E[0][0] + E[-1][0] <= W
        d1 = E[0][1] + E[-1][1] <= W
        dp[0][0] = 0 if d0 else 1
        dp[0][1] = 0 if d1 else 1
        dp[1][2] = min(dp[0][0] + 1, dp[0][1] + 1)
        dp[1][2] -= 1 if d0 and d1 else 0

        for i in range(1, N):

            dp[i][0] = dp[i][2] + 1
            dp[i][1] = dp[i][2] + 1

            b0 = E[i][0] + E[i-1][0] <= W
            b1 = E[i][1] + E[i-1][1] <= W
            if b0:
                dp[i][0] = min(dp[i][0], dp[i-1][1] + 1)
            if b1:
                dp[i][1] = min(dp[i][1], dp[i-1][0] + 1)

            dp[i+1][2] = min(dp[i][0] + 1, dp[i][1] + 1)
            if b0 and b1:
                dp[i+1][2] = min(dp[i+1][2], dp[i-1][2] + 2)
            if sum(E[i]) <= W:
                dp[i+1][2] = min(dp[i+1][2], dp[i][2] + 1)
        
        if d0 and d1:
            print(dp[N-1][2] + 2)
        elif d0:
            print(dp[N-1][1] + 1)
        elif d1:
            print(dp[N-1][0] + 1)
        else:
            print(dp[N][2])
        
        print(dp)

        

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