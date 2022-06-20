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

    def Msort(o, a, d):
        do, da = (1, 100) if d else (100, 1)

        mxm = 0

        for i in range(0, o*do, do):

            sav = dict()
            for e in brd[i:i+a*da:da]:
                if e in sav:
                    sav[e] += 1
                else:
                    sav[e] = 1
            if 0 in sav:
                del sav[0]

            res = []
            for t in sorted(sav.items(), key= lambda x: (x[1], x[0])):
                res.extend(t)
            res = res[:100]

            lim = max(a, len(res))
            mxm = max(mxm, len(res))
            brd[i:i+lim*da:da] = res + [0] * (lim-len(res))
        
        return mxm


    R, C, K = map(int, input().split())
    tgt = 100*R+C-101
    ans = -1
    brd = [0] * 10000
    rln, cln = 3, 3
    for y in range(0, 300, 100):
        brd[y:y+3] = map(int, input().split())
    
    for time in range(101):

        if brd[tgt] == K:
            ans = time
            break

        if rln >= cln:
            cln = Msort(rln, cln, 0)
        else:
            rln = Msort(cln, rln, 1)
    
    print(ans)

    # for y in range(0, 100*rln, 100): # 격자 확인용
    #     print(brd[y:y+cln])

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