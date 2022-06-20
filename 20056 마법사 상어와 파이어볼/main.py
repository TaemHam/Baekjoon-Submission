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
#from heapq import heappush, heapreplace
#import bisect
#from bisect import bisect_left as bl, bisect_right as br
DEBUG = False


def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    N, M, K = map(int, input().split())
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    brd = dict()
    que = [list(map(int, input().split())) for _ in range(M)]

    for _ in range(K):

        '''이동 페이즈'''
        brd.clear()
        for y, x, m, s, d in que:
            crd = (y+dy[d]*s)%N * N + (x + dx[d]*s)%N
            if crd not in brd:
                brd[crd] = [1, m, s, d%2, d]
            else:
                brd[crd][0] += 1
                brd[crd][1] += m
                brd[crd][2] += s
                brd[crd][3] += d%2
        
        '''융합 페이즈'''
        que.clear()
        for crd, (c, m, s, n, d) in brd.items():
            y, x = divmod(crd, N)
            if c == 1:
                que.append((y, x, m, s, d))
            else:
                if not m//5:
                    continue
                que.extend((y, x, m//5, s//c, i) for i in range(1 if n%c else 0, 8, 2))
    
    print(sum(i[2] for i in que))
                        
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