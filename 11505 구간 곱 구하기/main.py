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

    def sprd(l, r):
        res = 1
        l += h
        r += h
        
        while l <= r:
            if l % 2:
                res = res * grp[l] % mod
                l += 1
            if not r % 2:
                res = res * grp[r] % mod
                r -= 1
            l //= 2
            r //= 2
            
        return res

    def sudt(x, v):
        x += h
        grp[x] = v
        while x > 1:
            x //= 2
            grp[x] = grp[x*2] * grp[x*2+1] % mod

    n, m, k = map(int, input().split())
    m += k
    h = 2**(len(format(n-1, 'b')))
    mod = 1000000007
    grp = [1] * h * 2

    for i in range(n):
        grp[h+i] = int(input().strip())

    h -= 1
    
    for i in range(h, -1, -1):
        grp[i] = grp[2*i] * grp[2*i+1] % mod

    for _ in range(m):
        a, b, c = map(int, input().split())
        if a == 1:
            sudt(b, c)
        else:
            print(sprd(b, c))

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