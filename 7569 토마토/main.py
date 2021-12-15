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

    input = sys.stdin.readline
    n,m,k = map(int,input().split())
    mat = [[[] for _ in range(n)] for _ in range(m)]


    z_cnt_before = 0
    q = deque()
    for _ in range(k):
        for i in range(m):
            t = input().split()
            for j in range(n):
                mat[i][j].append(t[j])
                if t[j] == '1':
                    q.append((i,j,_))
                elif t[j] == '0':
                    z_cnt_before += 1

    dy = [1,-1,0,0,0,0]
    dx = [0,0,1,-1,0,0]
    dz = [0,0,0,0,1,-1]
    v = set()

    def bfs(q):
        z_cnt_after = 0
        cnt_d = len(q)
        cnt_u = 0

        while q:
            y,x,z = q.popleft()
            v.add((y,x,z))

            for i in range(6):
                ny = y + dy[i]
                nx = x + dx[i]
                nz = z + dz[i]

                if 0 <= ny < m and 0 <= nx < n and 0 <= nz < k:
                    if mat[ny][nx][nz] == '0' and (ny,nx,nz) not in v:
                        mat[ny][nx][nz] = '1'
                        q.append((ny,nx,nz))
                        z_cnt_after += 1

            cnt_d -= 1
            if cnt_d == 0 and len(q) != 0:
                cnt_u += 1
                cnt_d = len(q)
        return (cnt_u,z_cnt_after)
    
    cnt_u, z_cnt_after = bfs(q)
    if z_cnt_before != z_cnt_after:
        print(-1)
    else:
        print(cnt_u)


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