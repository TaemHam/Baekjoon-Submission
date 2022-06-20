# CP template Version 1.006
#import io
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
#from itertools import permutations
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
    #sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    def ccw(a, b, c):
        return ((b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0]))

    ans = []
    for _ in range(int(input().strip())):
        arr = []
        tmp = list(map(int, input().split()))
        for i in range(1, len(tmp), 2):
            arr.append((tmp[i], tmp[i+1], len(arr)))
        arr.sort()
        stk = []
        for crd in arr[::-1]:
            while len(stk) > 1 and ccw(stk[-2], stk[-1], crd) > 0:
                stk.pop()
            else:
                stk.append(crd)

        res = []
        p = len(stk)-1
        for crd in arr:
            if crd == stk[p]:
                p -= 1
            else:
                res.append(str(crd[2]))
        
        for crd in stk:
            res.append(str(crd[2]))
        
        ans.append(' '.join(res))

    return '\n'.join(ans)

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
    input = sys.stdin.readline #io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
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
    