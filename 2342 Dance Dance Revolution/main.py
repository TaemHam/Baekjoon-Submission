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

    cmd = list(map(int, input().split()))[:-1]
    move = ((0, 2, 2, 2, 2), (0, 1, 3, 4, 3), (0, 3, 1, 3, 4), (0, 4, 3, 1, 3), (0, 3, 4, 3, 1))
    dp= [[0] * 5 for _ in range(2)]
    dp[1][0] = 0
    dp[1][1] = dp[1][2] = dp[1][3] = dp[1][4] = 4 * len(cmd)
    stt, flg = 0, 0
    for i in cmd:
        print(i)
        for j in range(5):
            dp[flg][j] = dp[1-flg][j] + move[stt][i]
        print(dp)

        for j in range(5):
            dp[flg][stt] = min(dp[flg][stt], dp[1-flg][j] + move[j][i])
        
        stt = i
        flg = 1 - flg
        print(dp)
    
    print(min(dp[1 - flg]))


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