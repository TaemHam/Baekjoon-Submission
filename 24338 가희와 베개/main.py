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
#from bisect import bisect_left as bl
DEBUG = False

def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    N, M = map(int, input().split())
    L = M+1
    ans = -1
    mov = (1, -1, L, -L)
    ins = {'.':'EWSN', '1':'WENS'}
    flp = {'.':'1', '1':'.'}
    swt = []
    vis = [0] * N*L + [1] * L
    tgt = [0] * N*L
    brd = [0] * N*L
    for y in range(0, N*L, L):
        vis[y+M] = 1
        brd[y:y+M] = list(input().strip())
        for xy in range(y, y+M):
            if brd[xy] == '?':
                brd[xy] = 'E'
            elif brd[xy] == 'P' or brd[xy] == 'B':
                tgt[xy] = 1
                swt.append((xy, brd[xy]))
                brd[xy] = '.'
                
    x, y = map(lambda x: int(x)-1, input().split())
    que = [(x*L+y, brd[x*L+y], {})]

    for cur, hgt, rmp in que:
        if tgt[cur]:
            swt.extend(rmp.items())
            for loc, alp in swt:
                brd[loc] = alp
            ans = ''.join(brd[:M])
            for y in range(L, N*L, L):
                ans += '\n' + ''.join(brd[y:y+M])
            break

        for d in range(4):
            nxt = cur+mov[d]
            if not vis[nxt]:
                if brd[nxt] == 'E' and not vis[nxt+mov[d]] and brd[nxt+mov[d]] == flp[hgt] and nxt not in rmp:
                    vis[nxt+mov[d]] = 1
                    nrmp = rmp.copy()
                    nrmp[nxt] = ins[hgt][d]
                    que.append((nxt+mov[d], flp[hgt], nrmp))
                elif brd[nxt] == hgt:
                    vis[nxt] = 1
                    que.append((nxt, hgt, rmp))
     
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