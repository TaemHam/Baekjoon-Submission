# CP template Version 1.006
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
from itertools import combinations
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

    n, s= map(int, input().split())
    arr= list(map(int, input().split()))
    ar1, ar2= arr[:n//2], arr[n//2:]
    sa1, sa2= [], []

    for i in range(len(ar1)+1):
        t = combinations(ar1, i)
        for j in t:
            sa1.append(sum(j))

    for i in range(len(ar2)+1):
        t = combinations(ar2, i)
        for j in t:
            sa2.append(sum(j))

    sa1.sort()
    sa2.sort(reverse= True)

    p1, p2 = 0, 0
    ans = 0

    while p1 < len(sa1) and p2 < len(sa2):
        t = sa1[p1] + sa2[p2]
        if t == s:
            c1 = 1
            c2 = 1
            p1 += 1
            p2 += 1
            while p1 < len(sa1) and sa1[p1-1] == sa1[p1]:
                c1 += 1
                p1 += 1
            while p2 < len(sa2) and sa2[p2-1] == sa2[p2]:
                c2 += 1
                p2 += 1
            ans += c1 * c2
        elif t < s:
            p1 += 1
        else:
            p2 += 1

    if s == 0:
        ans -= 1
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