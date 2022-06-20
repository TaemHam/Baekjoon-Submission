# CP template Version 1.006
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
from itertools import combinations
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

    N, M, G, R = map(int, input().split())
    L = M+1
    ans = 0
    mov = (1, -1, L, -L)
    brd = ['0'] * N*L
    vis = [0] * N*L + [9999] * L
    v = 0
    cnd = []

    for y in range(0, N*L, L):
        vis[y+M] = 9999
        brd[y:y+M] = input().split()
        for xy in range(y, y+M):
            if brd[xy] == '2':
                cnd.append(xy)

    for pos in combinations(cnd, G+R):
        po = set(pos)
        for grn in combinations(pos, G):
            res = 0
            red = po - set(grn)

            for cur in pos:
                vis[cur] = v

            while True:

                nred = set()
                for cur in red:
                    for d in mov:
                        if vis[cur+d] < v and brd[cur+d] != '0' and cur+d not in nred:
                            nred.add(cur+d)
                
                ngrn = []
                for cur in grn:
                    for d in mov:
                        if vis[cur+d] < v and brd[cur+d] != '0':
                            vis[cur+d] = v
                            if cur+d in nred:
                                res += 1
                                nred.discard(cur+d)
                            else:
                                ngrn.append(cur+d)

                if not nred or not ngrn:
                    break

                for cur in nred:
                    vis[cur] = v

                red, grn = nred, ngrn

            ans = max(ans, res)
            v += 1
    
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