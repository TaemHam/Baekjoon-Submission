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
#from math import log2, ceil
#from heapq import heappush, heappop
#import bisect
#from bisect import bisect_left as bl, bisect_right as br
DEBUG = False


def main(f=None):
    init(f)
    #sys.setrecursionlimit(10**5)
    # ######## INPUT AREA BEGIN ##########

    def sgmt(stt, end, p):
        if stt == end:
            grp[p] = arr[stt]
            return grp[p]
        else:
            mid = (stt + end) // 2
            grp[p] = sgmt(stt, mid, p*2) + sgmt(mid + 1, end, p*2 + 1)
            return grp[p]

    def ssum(stt, end, p, l, r):
        if r < stt or end < l:
            return 0
            
        if l <= stt and end <= r:
            return grp[p]

        mid = (stt + end) // 2
        return ssum(stt, mid, p*2, l, r) + ssum(mid + 1, end, p*2 + 1, l, r)

    def sudt(stt, end, p, idx, dif):
        if idx < stt or end < idx:
            return
        
        grp[p] += dif

        if stt != end:
            mid = (stt + end) // 2
            sudt(stt, mid, p*2, idx, dif)
            sudt(mid + 1, end, p*2 + 1, idx, dif)

    n, m, k = map(int, input().split())
    arr = [0] + [int(input().strip()) for _ in range(n)]
    grp = [0] * (n*4)
    sgmt(1, n, 1)

    for _ in range(m+k):
        flg, a, b = map(int, input().split())
        
        if flg == 1:
            sudt(1, n, 1, a, b - arr[a])
            arr[a] = b
        
        if flg == 2:
            print(ssum(1, n, 1, a, b))

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