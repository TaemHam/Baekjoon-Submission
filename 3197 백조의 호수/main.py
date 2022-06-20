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
#from bisect import bisect_left as bl, bisect_right as br
DEBUG = False


def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    R, C = map(int, input().split())
    L = C+1
    mov = (1, -1, L, -L)
    brd = ['#'] * (R+1)*L
    cswn = []
    cque = []
    for y in range(0, R*L, L):
        brd[y:y+C] = list(input().rstrip())
        for xy in range(y, y+C):
            if brd[xy] == '.':
                cque.append(xy)
            if brd[xy] == 'L':
                brd[xy] = '.'
                cque.append(xy)
                cswn.append(xy)
    brd[cswn[0]] = '#'
    tgt = cswn.pop()

    for time in range(R+C):
        
        '''찾기 페이즈'''
        nswn = []
        for cur in cswn:
            flg = 0
            if cur == tgt:
                return time
            for dir in mov:
                if brd[cur+dir] == '.':
                    brd[cur+dir] = '#'
                    cswn.append(cur+dir)
                elif brd[cur+dir] == 'X' and not flg:
                    nswn.append(cur)
                    flg = 1
        cswn = nswn

        '''녹이기 페이즈'''
        nque = []
        for cur in cque:
            for dir in mov:
                if brd[cur+dir] == 'X':
                    brd[cur+dir] = '.'
                    nque.append(cur+dir)
        cque = nque

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