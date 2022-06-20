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

    ans = []
    N = int(input())
    h = 1<<len(format(N-1, 'b'))
    seg = [int(1e9)]*h + list(map(int, input().split())) + [int(1e9)]*(h-N)
    h -= 1
    
    for i in range(h, 0, -1):
        seg[i] = min(seg[i*2], seg[i*2+1])
    
    for _ in range(int(input())):
        a, b, c = map(int, input().split())
        if a == 1:
            b = b+h
            seg[b] = c
            while b:
                b >>= 1
                seg[b] = min(seg[b*2], seg[b*2+1])
        else:
            b, c = b+h, c+h
            res = int(1e9)
            while b <= c:
                if b & 1:
                    res = min(res, seg[b])
                    b += 1
                if not c & 1:
                    res = min(res, seg[c])
                    c -= 1
                b >>= 1
                c >>= 1
            ans.append(str(res))
        
    print('\n'.join(ans))

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