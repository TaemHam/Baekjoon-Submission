# CP template Version 1.006
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
#from bisect import bisect_left as bl, bisect_roloc[xyight as brloc[xy]
DEBUG = False

def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    K = int(input().strip()) * 4
    L = K+1
    siz = L*L
    mov = (0, 1, -1, L, -L)
    brd = ['#'] * siz*8
    vis = [0] * siz*8
    tgt = siz*8-1

    for y in range(0, K*L, L):
        brd[y:y+K] = input().strip()

    for m in range(K//4):
        for n in range(K//4):
            flg = (m&1) ^ (n&1)
            for y in range(4):
                for x in range(4):
                    if brd[4*m*L+4*n+y*L+x] == '#':
                        continue
                    elif brd[4*m*L+4*n+y*L+x] == 'E':
                        brd[siz*(flg*4)+4*m*L+4*n+y*L+x], brd[siz*(flg*4+1)+4*m*L+4*n+3-y+x*L], brd[siz*(flg*4+2)+4*m*L+4*n+3+3*L-y*L-x], brd[siz*(flg*4+3)+4*m*L+4*n+3*L+y-x*L] =\
                            [tgt] * 4
                    else:
                        if brd[4*m*L+4*n+y*L+x] == 'S':
                            cque = [4*m*L+4*n+y*L+x]
                        brd[siz*(flg*4)+4*m*L+4*n+y*L+x], brd[siz*(flg*4+1)+4*m*L+4*n+3-y+x*L], brd[siz*(flg*4+2)+4*m*L+4*n+3+3*L-y*L-x], brd[siz*(flg*4+3)+4*m*L+4*n+3*L+y-x*L] =\
                            siz*(flg*4+1)+4*m*L+4*n+3-y+x*L, siz*(flg*4+2)+4*m*L+4*n+3+3*L-y*L-x, siz*(flg*4+3)+4*m*L+4*n+3*L+y-x*L, siz*(flg*4)+4*m*L+4*n+y*L+x

    for m in range(K//4):
        for n in range(K//4):
            for y in range(4):
                for x in range(4):
                    if (m&1) ^ (n&1):
                        for i in range(4):
                            brd[4*m*L+4*n+y*L+x+siz*i] = brd[4*m*L+4*n+y*L+x+siz*4]
                    else:
                        for i in range(4, 8):
                            brd[4*m*L+4*n+y*L+x+siz*i] = brd[4*m*L+4*n+y*L+x]

    for time in range(len(brd)):
        nque = []
        for cur in cque:
            if cur == tgt:
                return time
            for d in mov:
                if brd[cur+d] != '#' and not vis[brd[cur+d]]:
                    vis[brd[cur+d]] = 1
                    nque.append(brd[cur+d])
        
        if not nque:
            break
        cque = nque

    return -1
                

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
    print(main())
    