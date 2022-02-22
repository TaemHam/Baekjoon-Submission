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

    N = int(input().strip())
    dy = [0, 1, 0, -1]
    dx = [-1, 0, 1, 0]
    dd = [(2, 0, 0.05), (1, 1, 0.1), (0, 1, 0.07), (0, 2, 0.02), (-1, 1, 0.01)]
    brd = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    f, d, c = 1, 0, 1
    flg_a, flg_b = 2, 1
    y, x = N//2, N//2

    for _ in range(1, N**2):
        y += dy[d]
        x += dx[d]
        
        snd_psh = brd[y][x]

        if brd[y][x] >= 10:
            for i in range(1, 10):
                f *= -1
                i //= 2
                fwd, sde, pct = dd[i]
                snd_mov = int(brd[y][x] * pct)
                if snd_mov:
                    snd_psh -= snd_mov
                    td = (d + f) % 4
                    ny = y + fwd * dy[d] + sde * dy[td]
                    nx = x + fwd * dx[d] + sde * dx[td]
                    if 0 <= ny < N and 0 <= nx < N:
                        brd[ny][nx] += snd_mov
                    else:
                        ans += snd_mov
        
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= ny < N and 0 <= nx < N:
            brd[ny][nx] += snd_psh
        else:
            ans += snd_psh
        
        brd[y][x] = 0

        c -= 1
        if not c:
            d = (d + 1) % 4
            flg_a -= 1
            if not flg_a:
                flg_a = 2
                flg_b += 1
            c = flg_b

    print(ans)

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