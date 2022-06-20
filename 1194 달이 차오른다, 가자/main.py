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
    vis = [[0] * (N+1)*L for _ in range(64)]
    mov = [1, -1, L, -L]
    brd = ['#'] * (N+1)*L 
    ans = -1

    for y in range(0, N*L, L):
        brd[y:y+M] = list(input().strip())
    
    cque = [(brd.index('0'), 0)]
    brd[cque[0][0]] = '.'

    for time in range(1, 100000):
        nque = []
        for cur, inv in cque:
            for d in mov:
                nxt = cur+d
                if not vis[inv][nxt] and brd[nxt] != '#':

                    if brd[nxt] == '.':
                        nque.append((nxt, inv))
                        vis[inv][nxt] = 1

                    elif brd[nxt] == '1':
                        ans = time
                        cque.clear()
                        nque = []
                        break

                    elif brd[nxt].islower():
                        vis[inv][nxt] = 1
                        ninv = inv | 1 << ord(brd[nxt])-97
                        nque.append((nxt, ninv))
                        vis[ninv][nxt] = 1

                    else: 
                        if inv & 1 << ord(brd[nxt])-65:
                            nque.append((nxt, inv))
                            vis[inv][nxt] = 1
        if not nque:
            break
        cque = nque

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