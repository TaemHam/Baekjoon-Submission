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

    def catch(cur):
        for dep in range(R):
            if brd[dep][cur]:
                num = brd[dep][cur]
                del shk[num]
                brd[dep][cur] = 0
                return num
        return 0
    
    def up(r, c, s, d):
        r -= s
        if r < 0:
            r = -r
            d = 2
        return r, c, s, d

    def dwn(r, c, s, d):
        r += s
        if r >= R:
            r = rl-r
            d = 1
        return r, c, s, d

    def rgt(r, c, s, d):
        c += s
        if c >= C:
            c = cl-c
            d = 4
        return r, c, s, d

    def lft(r, c, s, d):
        c -= s
        if c < 0:
            c = -c
            d = 3
        return r, c, s, d

    R, C, M = map(int, input().split())
    rl, cl = (R-1)*2, (C-1)*2
    ans = 0
    run = []
    shk = {}
    mov = (0, up, dwn, rgt, lft)
    flp = (0, 2, 1, 4, 3)
    brd = [[0] * C for _ in range(R)]

    for _ in range(M):
        r, c, s, d, z = map(int, input().split())
        r, c = r-1, c-1
        if d//3:
            s %= cl
            if s >= C:
                s = cl-s
                d = flp[d]
        else:
            s %= rl
            if s >= R:
                s = rl-s
                d = flp[d]
        shk[z] = (r, c, s, d)
        brd[r][c] = z
    
    for cur in range(C-1):

        ans += catch(cur)

        nxt = [[0] * C for _ in range(R)]
        for z in shk:
            r, c, s, d = mov[shk[z][3]](*shk[z])
            shk[z] = (r, c, s, d)
            if nxt[r][c]:
                if nxt[r][c] < z:
                    nxt[r][c], z = z, nxt[r][c]
                run.append(z)
            else:
                nxt[r][c] = z

        while run:
            del shk[run.pop()]
        brd = nxt
    
    print(ans + catch(C-1))
        
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