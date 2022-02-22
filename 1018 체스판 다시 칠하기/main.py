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
    brd = [[0]*m for _ in range(n)]                             # brd에 흰색 1, 검은색 0으로 저장
    for y in range(n):
        t = input().strip()
        for x in range(m):
            if t[x] == 'W':
                brd[y][x] = 1

    pick = brd[0][0]                                            # brd의 첫 칸 색을 기준으로
    grp = [[0]*m for _ in range(n)]                             # 각각의 칸마다 색칠해야하면 1로, 놔둬도 되면 0으로 grp에 저장
    for y in range(n):
        flg = (y%2 - pick)%2
        for x in range(m):
            if brd[y][x] != flg:
                grp[y][x] = 1
            flg = 1 - flg
    
    dp1 = [[0]*m for _ in range(n-7)]                           # dp1은 세로 8칸 합 저장 용도
    for x in range(m):
        dp1[0][x] = sum([grp[i][x] for i in range(8)])
        for y in range(1, n-7):
            dp1[y][x] = dp1[y-1][x] - grp[y-1][x] + grp[y+7][x]
    
    dp2 = [[0]*(m-7) for _ in range(n-7)]                       # dp2에 8x8칸 합 저장
    ans = 32
    for y in range(len(dp1)):
        t = sum(dp1[y][i] for i in range(8))
        ans = min(ans, t, 64-t)                                 # 64에서 빼주는 이유는 
        dp2[y][0] = t                                           # 다른 색으로 칠하는 경우를 고려해야 하기 때문
        for x in range(1, m-7):
            t = dp2[y][x-1] - dp1[y][x-1] + dp1[y][x+7]
            ans = min(ans, t, 64-t)
            dp2[y][x] = t

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