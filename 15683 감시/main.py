# CP template Version 1.006
#import io
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
#from bisect import insort_left as il
DEBUG = False


def main(f=None):
    init(f)
    # ######## INPUT AREA BEGIN ##########

    def cover(dir, loc, sav):
        loc += dir
        while oob[loc] and loc not in wll:
            sav.add(loc)
            loc += dir
        return sav
    
    def max_cvr(idx, cvr):
        if idx == len(cams):
            return len(cvr)

        max_val = 0
        for i in cams[idx]:
            max_val = max(max_val, max_cvr(idx+1, cvr.union(i)))
        return max_val

    dd = [1, 10, -1, -10]
    N, M = map(int, input().split())
    siz = N * 10 + M
    cams = []
    cam5 = []
    wll = set()
    cvr = set()
    oob = [0] * siz
    for y in range(0, N*10, 10):
        oob[y:y+M] = [1] * M

        for x, e in enumerate(map(int, input().split())):
            
            if e == 0:
                continue
            elif e == 5:
                cam5.append(y+x)
            elif e == 6:
                wll.add(y+x)
            else:
                cams.append((y+x, e))
            cvr.add(y+x)

    for loc in cam5:
        for i in range(4):
            cvr = cover(dd[i], loc, cvr)
    
    for idx, (loc, cam) in enumerate(cams):
        sav = []
        if cam == 1:
            for i in range(4):
                sav.append(cover(dd[i], loc, set()))
        elif cam == 2:
            for i in range(2):
                sav.append(cover(dd[i+2], loc, cover(dd[i], loc, set())))
        elif cam == 3:
            for i in range(-4, 0):
                sav.append(cover(dd[i+1], loc, cover(dd[i], loc, set())))
        elif cam == 4:
            for i in range(-4, 0):
                sav.append(cover(dd[i+2], loc, cover(dd[i+1], loc, cover(dd[i], loc, set()))))
                
        cams[idx] = sav

    print(N*M - max_cvr(0, cvr))


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