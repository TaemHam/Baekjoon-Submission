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
#from bisect import bisect_left as bl
DEBUG = False


def main(f=None):
    init(f)
    # ######## INPUT AREA BEGIN ##########

    tbl = [[0, 
         2,  4,  6,  8, 10,
        12, 14, 16, 18, 20,
        22, 24, 26, 28, 30,
        32, 34, 36, 38, 40] + [0]*5,
        [10, 13, 16, 19, 25, 30, 35, 40] + [0]*5,
        [20, 22, 24, 25, 30, 35, 40] + [0]*5,
        [30, 28, 27, 26, 25, 30, 35, 40] + [0]*5]
    loc = [list(range(21)) + [99]*5,
        [5, 21, 22, 23, 24, 25, 26, 20] + [99]*5,
        [10, 27, 28, 24, 25, 26, 20] + [99]*5,
        [15, 29, 30, 31, 24, 25, 26, 20] + [99]*5]
    fnd = [
        (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (0, 6), (0, 7), (0, 8), (0, 9), (2, 0),
        (0, 11), (0, 12), (0, 13), (0, 14), (3, 0), (0, 16), (0, 17), (0, 18), (0, 19), (0, 20),
        (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 2), (3, 1), (3, 2), (3, 3)]

    dgt = [1, 100, 10000, 1000000]

    nque = [(0, 0, 0)] # 점수, 말의 위치, 보드 현황 저장
    cque = []
    ans = (0, 0, 0)

    for mov in map(int, input().split()):

        nque, cque = cque, nque

        while cque:
            scr, tkn, brd = cque.pop()
            vis = set()
            for i in dgt:
                cur = tkn // i % 100
                if cur != 99 and cur not in vis:
                    vis.add(cur)
                    nxt = loc[fnd[cur][0]][fnd[cur][1] + mov]
                    if nxt != 99 and not brd & (1<<nxt):
                        nque.append((scr + tbl[fnd[nxt][0]][fnd[nxt][1]], tkn - cur*i + nxt*i, brd & ~(1<<cur) | (1<<nxt)))
                    elif nxt == 99:
                        nque.append((scr, tkn - cur*i + nxt*i, brd & ~(1<<cur)))

        ans = max(nque + [ans], key= lambda x: x[0])
    
    print(ans[0])


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
    main()