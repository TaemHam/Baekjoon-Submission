# CP template Version 1.006
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
#from itertools import product
#import collections
from collections import deque
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

m, n = list(map(int,input().split()))
mat = [[-1]*(m+2)]+[[-1]+list(map(int,sys.stdin.readline().split()))+[-1] for _ in range (n)]+[[-1]*(m+2)]
grp = {}
que = deque()
zcnt = 0
for i in range(1,n+1): #i는 가로행
    for j in range(1,m+1): #j는 세로열
        if mat[i][j] == 1: que.append((i,j))
        elif mat[i][j] == 0: zcnt += 1
        if mat[i][j] !=-1:
            movp = []
            if mat[i-1][j] != -1: movp.append((i-1,j))
            if mat[i+1][j] != -1: movp.append((i+1,j))
            if mat[i][j-1] != -1: movp.append((i,j-1))
            if mat[i][j+1] != -1: movp.append((i,j+1))
            grp[(i,j)] = movp
if zcnt != 0:
    day = 0
    size = len(que)
    cnt = 0
    while que:
        if size == cnt:
            day+=1
            size = len(que)
            cnt = 0
        cur = que.popleft()
        cnt += 1
        if cur in grp:
            que += [i for i in grp[cur]]
            del grp[cur]
    else: day -= 1
    if len(grp) != 0: print(-1)
    else: print(day)
else: print(0)
            


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