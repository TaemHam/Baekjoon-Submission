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

    def turn(a, b, c, d):
        brd[a], brd[b], brd[c], brd[d] = brd[b], brd[c], brd[d], brd[a]

    N, _ = map(int, input().split())
    L = N+1
    ans = 0
    dir = (L, -1, -L, 1)
    brd = [-1] * L*L
    for y in range(0, N*L, L):
        brd[y:y+N] = map(int, input().split())
    
    for _ in range(200):
        boom = ([0], 0)
        vis = [0] * L*L
        for y in range(0, N*L, L):
            for xy in range(y, y+N):
                if brd[xy] > 0 and not vis[xy]:
                    vis[xy] = 1
                    que = [xy]
                    rnb = []
                    for cur in que:
                        for d in dir:
                            if (brd[cur+d] == brd[xy] or brd[cur+d] == 0) and not vis[cur+d]:
                                if brd[cur+d] == 0:
                                    rnb.append(cur+d)
                                que.append(cur+d)
                                vis[cur+d] = 1
                    boom = max(boom, (que, len(rnb)) , key= lambda x: (len(x[0]), x[1], x[0][0]))
                    for loc in rnb:
                        vis[loc] = 0
        if len(boom[0]) >= 2:
            ans += len(boom[0]) ** 2
            for loc in boom[0]:
                brd[loc] = -2
        else:
            break
        
        for x in range(N*L-L, N*L):
            cur = x
            for nxt in range(x, -1, -L):
                if brd[nxt] == -2:
                    continue
                elif brd[nxt] == -1:
                    cur = nxt - L
                else:
                    brd[cur], brd[nxt] = brd[nxt], brd[cur]
                    cur -= L

        for i in range(L//2):
            xy = i*L + i
            j = N-i*2-1
            lt, rt, rb, lb = xy, xy+j, xy+j*L+j, xy+j*L
            for k in range(j):
                turn(k+lt, k*L+rt, -k+rb, -k*L+lb)

        for x in range(N*L-L, N*L):
            cur = x
            for nxt in range(x, -1, -L):
                if brd[nxt] == -2:
                    continue
                elif brd[nxt] == -1:
                    cur = nxt - L
                else:
                    brd[cur], brd[nxt] = brd[nxt], brd[cur]
                    cur -= L
    
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