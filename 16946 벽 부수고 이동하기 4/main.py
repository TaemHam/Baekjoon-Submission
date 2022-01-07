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

    n, m = map(int, input().split())
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    grp = [[-i for i in list(map(int, list(input().strip())))] for _ in range(n)]
    D = [0]
    ans = [[] for _ in range(n)]

    def dfs(q, num):
        if grp[q[0][0]][q[0][1]] != 0:
            return False
        grp[q[0][0]][q[0][1]] = num
        D.append(1)
        while q:
            y, x = q.pop()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0<=ny<n and 0<=nx<m and grp[ny][nx] == 0:
                    grp[ny][nx] = num
                    D[num] += 1
                    q.append((ny, nx))
        return True

    num = 1
    for y in range(n):
        for x in range(m):
            if grp[y][x] == 0:
                if dfs([(y, x)], num):
                    num += 1
    
    for y in range(n):
        for x in range(m):
            if grp[y][x] == -1:
                t = set()
                tv= 1
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if 0<=ny<n and 0<=nx<m and grp[ny][nx] != -1:
                        t.add(grp[ny][nx])
                for i in t:
                    tv += D[i]
                ans[y].append(tv%10)
            else:
                ans[y].append(0)

    for i in ans:
        print(''.join(map(str, i)))


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