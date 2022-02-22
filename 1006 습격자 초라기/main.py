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
    # sys.setfillsionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    def fill(stt, a, b, c):
        for i in range(stt, N):
            a[i+1] = min(b[i]+1, c[i]+1)
            if l1[i] + l2[i] <= W: 
                a[i+1] = min(a[i+1], a[i]+1)
            if i > 0 and l1[i-1] + l1[i] <= W and l2[i-1] + l2[i] <= W: 
                a[i+1] = min(a[i+1], a[i-1]+2)

            if i < N-1:
                b[i+1] = a[i+1] + 1
                if l1[i+1] + l1[i] <= W: 
                    b[i+1] = min(b[i+1], c[i] + 1)

                c[i+1] = a[i+1]+1
                if l2[i+1] + l2[i] <= W: 
                    c[i+1] = min(c[i+1], b[i] + 1)

        return a, b, c

    TC = int(input().strip())

    for _ in range(TC):
        N, W = map(int, input().split())
        l1 = list(map(int, input().split()))
        l2 = list(map(int, input().split()))

        a = [0 for _ in range(N+1)]
        b = [0 for _ in range(N+1)]
        c = [0 for _ in range(N+1)]
        a[0] = 0
        b[0] = 1
        c[0] = 1
        a, b, c = fill(0, a, b, c)
        ans = a[N]
    
        if N > 1 and l1[0] + l1[N-1] <= W:
            a[1] = 1
            b[1] = 2

            if l2[0] + l2[1] <= W:
                c[1] = 1
            else: 
                c[1] = 2

            a, b, c = fill(1, a, b, c)
            ans = min(ans, c[N-1] + 1)

        if N > 1 and l2[0] + l2[N-1] <= W:
            a[1] = 1
            c[1] = 2

            if l1[0] + l1[1] <= W: 
                b[1] = 1 
            else: 
                b[1] = 2

            a, b, c = fill(1, a, b, c)
            ans = min(ans, b[N-1] + 1)

        if N > 1 and l1[0] + l1[N-1] <= W and l2[0] + l2[N-1] <= W:
            a[1] = 0
            b[1] = 1
            c[1] = 1

            a, b, c = fill(1, a, b, c)
            ans = min(ans, a[N-1] + 2)

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