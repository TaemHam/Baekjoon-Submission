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

    def ccw(a, b, c):
        t = (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])
        if t > 0:
            return 1
        elif t == 0 :
            return 0
        else:
            return -1
    
    def cross():
        print(1)

        a = (x4 - x3) * (y2 - y1) - (x2 - x1) * (y4 - y3)

        if a:
            x = ((x1 * y2 - y1 * x2) * (x4 - x3) - (x3 * y4 - y3 * x4) * (x2 - x1)) / a
            y = ((x1 * y2 - y1 * x2) * (y4 - y3) - (x3 * y4 - y3 * x4) * (y2 - y1)) / a

        else:
            if (x1, y1) == (x4, y4) and (x3, y3) <= (x1, y1):
                x, y = x1, y1
            elif (x2, y2) == (x3, y3) and (x1, y1) <= (x3, y3):
                x, y = x2, y2
            else:
                return
                
        print(x, y)

    x1, y1, x2, y2 = map(float, input().split())
    x3, y3, x4, y4 = map(float, input().split())

    d12 = ccw((x1, y1), (x2, y2), (x3, y3)) * ccw((x1, y1), (x2, y2), (x4, y4))
    d34 = ccw((x3, y3), (x4, y4), (x1, y1)) * ccw((x3, y3), (x4, y4), (x2, y2))

    if d12 == 0 and d34 == 0:
        if (x1, y1) > (x2, y2):
            x1, y1, x2, y2 = x2, y2, x1, y1
        if (x3, y3) > (x4, y4):
            x3, y3, x4, y4 = x4, y4, x3, y3

        if (x1, y1) <= (x4, y4) and (x3, y3) <= (x2, y2):
            cross()
            return

    elif d12 <= 0 and d34 <= 0:
        cross()
        return
    
    print(0)


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