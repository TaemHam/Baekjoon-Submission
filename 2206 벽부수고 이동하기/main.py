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
    # ######## INPUT AREA END ############

    n,m = map(int,input().split())
    g = [sys.stdin.readline().strip() for _ in range(n)]
    inf = 987654321
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    q1 = [(0,0)]
    q2 = [(m-1,n-1)]
    d1 = d2 = [[inf for _ in range(m)] for _ in range(n)]


    while q1:
        x,y = q1.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and d1[nx][ny] == inf:
                d1[nx][ny] = d1[x][y] + 1
                if g[nx][ny] == '0':
                    q1.append((nx,ny))


    while q2:
        x,y = q2.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and d2[nx][ny] == inf:
                d2[nx][ny] = d2[x][y] + 1           
                if g[nx][ny] == '0':
                    q2.append((nx,ny))
    

    ans = d1[-1][-1]
    for i in range(m):
        for j in range(n):
            if g[i][j] == '1':
                ans = min(ans, d1[i][j] + d2[i][j])
    if ans == inf:
        print(-1)
    else:
        print(ans)




    


####    n,m = map(int,input().split())
    ####g = [list(map(int,list(sys.stdin.readline().strip()))) for _ in range(n)]

    ####dx = [1,-1,0,0]
    ####dy = [0,0,1,-1]

    ####def bfs():
        ####q = deque()
        ####q.append([0,0,1])
        ####v = [[[0,0] for i in range(m)] for j in range(n)]
        ####v[0][0][1] = 1

        ####while q:
            ####x,y,w = q.popleft()
            ####if x == n-1 and y == m-1:
                ####return v[x][y][w]

            ####for i in range(4):
                ####nx = x + dx[i]
                ####ny = y + dy[i]
                ####if 0<=nx<n and 0<=ny<m:
                    ####if g[nx][ny] == 1 and w == 1:
                        ####v[nx][ny][0] = v[x][y][1] + 1
                        ####q.append([nx,ny,0])
                    ####elif g[nx][ny] == 0 and v[nx][ny][w] == 0:
                        ####v[nx][ny][w] = v[x][y][w] + 1
                        ####q.append([nx,ny,w])
        ####return -1

    ####ans = bfs()
    ####print(ans)
                

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