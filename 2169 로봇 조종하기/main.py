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
#from bisect import bisect_left as bl
DEBUG = False

def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    N, M = map(int, input().split())

    '''첫줄'''
    brd = list(map(int, input().split()))
    dpu = [0] * M
    for i in range(M):
        dpu[i] = brd[i] + dpu[i-1]
    
    '''중간줄'''
    for _ in range(N-2):
        brd = list(map(int, input().split()))
        dpl = [-int(1e9)] * M
        dpr = [-int(1e9)] * M

        for i in range(M):
            dpl[i] = max(dpu[i], dpl[i-1]) + brd[i]
        for i in range(-1, -M-1, -1):
            dpr[i] = max(dpu[i], dpr[i+1]) + brd[i]
        
        dpu = list(max(dpl[i], dpr[i]) for i in range(M))
        
    '''마지막줄'''
    if N > 1:
        brd = list(map(int, input().split()))
        dpd = [0] * M
        for i in range(-1, -M-1, -1):
            dpd[i] = brd[i] + dpd[i+1]
        ans = max(sum(i) for i in zip(dpu, dpd))
    
    else:
        ans = dpu[-1]
    
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