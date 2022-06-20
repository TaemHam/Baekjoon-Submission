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
    L = N+1
    MAX = N*L
    mov = (1, -1, L, -L)
    vis = [0] * MAX + [1000] * L
    brd = [0] * MAX
    ans = 0
    stm = 0
    siz = 2
    for y in range(0, MAX, L):
        vis[y+N] = 1000
        brd[y:y+N] = map(int, input().split())
    loc = brd.index(9)
    cque = [loc]
    brd[loc] = 0

    for v in range(1, MAX):

        eat = MAX
        for sec in range(1, MAX//2):
            nque = []
            for cur in cque:
                for d in mov:
                    if vis[cur+d] < v and brd[cur+d] <= siz:
                        if 0 < brd[cur+d] < siz:
                            eat = min(eat, cur+d)
                        else:
                            vis[cur+d] = v
                            nque.append(cur+d)
            if eat != MAX:
                break
            cque = nque
        
        if eat == MAX:
            break
        
        cque = [eat]
        ans += sec
        brd[eat] = 0
        stm += 1
        if stm == siz:
            stm = 0
            siz += 1

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
    input = sys.stdin.readline  # by default
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