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
    #sys.setrecursionlimit(10**4)
    # ######## INPUT AREA BEGIN ##########            

    N = int(input().strip())
    prv = list(range(7))
    cur = [0] * 7
    scr = [0] * 7
    for _ in range(N):
        a1, b1, c1, b2, c2, a2 = map(int, input().split())
        cur[a1] = a2
        cur[a2] = a1
        cur[b1] = b2
        cur[b2] = b1
        cur[c1] = c2
        cur[c2] = c1
        for i in range(1, 7):
            scr[i] += 4 if prv[i] + cur[prv[i]] == 11 else \
                      5 if prv[i] == 6 or cur[prv[i]] == 6 else \
                      6
            prv[i] = cur[prv[i]]
    
    return max(scr)
    
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