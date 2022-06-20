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

    dd = [0, 1, -1, -100, 100]
    N, M, Y, X, _ = map(int, input().split())
    siz = 100 * N + M
    cur = 100 * Y + X
    ans = []
    brd = [0] * siz
    oob = [1] * siz
    for y in range(0, 100*N, 100):
        oob[y:y+M] = [0] * M
        brd[y:y+M] = list(map(int, input().split()))

    top, bot, lft, rgt, frt, bak = 0, 0, 0, 0, 0, 0
    
    for cmd in map(int, input().split()):
        if oob[cur + dd[cmd]]:
            continue

        cur += dd[cmd]

        if cmd == 1:
            top, lft, bot, rgt = lft, bot, rgt, top
        elif cmd == 2:
            top, lft, bot, rgt = rgt, top, lft, bot
        elif cmd == 3:
            top, frt, bot, bak = frt, bot, bak, top
        else: # cmd == 4:
            top, frt, bot, bak = bak, top, frt, bot

        ans.append(str(top))

        if not brd[cur]:
            brd[cur] = bot
        else:
            bot, brd[cur] = brd[cur], 0

    print('\n'.join(ans))

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