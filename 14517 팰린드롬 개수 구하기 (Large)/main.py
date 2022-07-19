# CP template Version 1.006
#import io
import os
import sys
#import string
#from functools import cmp_to_key
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


    def udt(k, v):
        while k < len(grp):
            grp[k] = (grp[k] + v) % mod
            k += k&-k

    def qry(k):
        r = 0
        while k:
            r = (r + grp[k]) % mod
            k -= k&-k
        return r

    S = input().strip()
    num = [0]
    for a in S:
        num.append(ord(a) - 97)

    loc = [[] for _ in range(26)]
    grp = [0] * (len(num))
    ans = len(S)
    mod = 10007

    for idx in range(1, len(num)):
        res = 0

        for adx in loc[num[idx]]:
            tmp = (idx - adx + qry(idx) - qry(adx)) % mod
            udt(adx, tmp)
            res = (res + tmp) % mod

        loc[num[idx]].append(idx)
        ans = (ans + res) % mod

    return ans

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