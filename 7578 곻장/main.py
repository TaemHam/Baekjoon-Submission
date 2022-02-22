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

    n = int(input().strip())
    h = 2 ** (len(format(n, 'b')))
    tree = [0] * 2*h
    h -= 1
    ans = 0
    arr_A = input().split()
    arr_B = input().split()
    num_d = dict()
    for i in range(n):
        num_d[arr_A[i]] = i

    x = h + num_d[arr_B[0]]
    tree[x] = 1
    while x > 1:
        x //= 2
        tree[x] += 1

    for i in range(1, n-1):
        t = num_d[arr_B[i]]
        l, r = h+t+1, h+n
        while l <= r:
            if l % 2:
                ans += tree[l]
                l += 1
            if not r % 2:
                ans += tree[r]
                r -= 1
            l //= 2
            r //= 2
        
        x = h+t
        tree[x] = 1
        while x > 1:
            x //= 2
            tree[x] += 1
    
    l, r = h+num_d[arr_B[-1]]+1, h+n
    while l <= r:
        if l % 2:
            ans += tree[l]
            l += 1
        if not r % 2:
            ans += tree[r]
            r -= 1
        l //= 2
        r //= 2
    
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