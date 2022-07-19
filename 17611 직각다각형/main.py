# CP template Version 1.006
import io
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
#from heapq import heappush, heappop
#import bisect
#from bisect import insort_left as il
DEBUG = False

def main(f=None):
    init(f)
    # ######## INPUT AREA BEGIN ##########

    def solving(ar1, ar2):
        prv = ar2[0]
        cnum = 0
        c1 = c2 = 0
        res = 0

        while c2 != len(ar2)-1:
            pnum = 0
            while ar2[c2] == prv:
                c2 += 1
                pnum += 1
            while ar1[c1] <= prv:
                c1 += 1
                cnum += 1
            res = max(res, cnum)
            cnum -= pnum
            prv = ar2[c2]
        
        return res

    def sorting(arr):
        arr.sort()
        arr.append(int(1e9))
    
    def saving(a, b):
        if a[0] != b[0]:
            a, b = sorted([a[0], b[0]])
            vl.append(a)
            vr.append(b-1)
        elif a[1] != b[1]:
            a, b = sorted([a[1], b[1]])
            hl.append(a)
            hr.append(b-1)

    N = int(input().strip())
    crd = [tuple(map(int, input().split())) for _ in range(N)]
    hl, hr, vl, vr = [], [], [], []
    
    for i in range(N-1, -1, -1):
        saving(crd[i], crd[i-1])

    for arr in [hl, hr, vl, vr]:
        sorting(arr)
    
    return(max(solving(vl, vr), solving(hl, hr)))

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
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline 
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