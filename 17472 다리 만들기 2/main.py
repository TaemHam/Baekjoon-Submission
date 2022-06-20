# CP template Version 1.006
#import io
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
    # sys.setrecursionlimit(10 ** 9)
    # ######## INPUT AREA BEGIN ##########

    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    N, M = map(int, input().split())
    brd = [input().split() for _ in range(N)]
    grp = [[9] * 7 for _ in range(7)]
    num = 1

    y_prv = [(0, 0) for _ in range(M)]
    for y in range(N):
        x_prv = (0, 0)
        for x in range(M):
            # 섬 번호 매기기
            if brd[y][x] == '1':
                brd[y][x] = num
                q = [(y, x)]
                while q:
                    ty, tx = q.pop()
                    for i in range(4):
                        ny = ty + dy[i]
                        nx = tx + dx[i]
                        if 0 <= ny < N and 0 <= nx < M and brd[ny][nx] == '1':
                            brd[ny][nx] = num
                            q.append((ny, nx))
                num += 1

            if type(brd[y][x]) is int:
                # 가로 거리 측정
                c, (p, d) = brd[y][x], x_prv
                if p != c:
                    if c > p:
                        c, p = p, c
                    dst = x - d - 1
                    if 2 <= dst < grp[c][p]:
                        grp[c][p] = dst
                x_prv = (brd[y][x], x)

                # 세로 거리 측정
                c, (p, d) = brd[y][x], y_prv[x]
                if p != c:
                    if c > p:
                        c, p = p, c
                    dst = y - d - 1
                    if 2 <= dst < grp[c][p]:
                        grp[c][p] = dst
                y_prv[x] = (brd[y][x], y)

    # 크루스칼 알고리즘
    def find(x):
        if x != par[x]:
            par[x] = find(par[x])
        return par[x]

    edg = []
    par = list(range(num))
    ans = 0

    for i in range(1, num-1):
        for j in range(i+1, num):
            if grp[i][j] != 9:
                edg.append((grp[i][j], i, j))

    for dst, a, b in sorted(edg):

        a = find(a)
        b = find(b)
        if a != b:
            if a > b:
                a, b = b, a
            par[b] = a
            ans += dst
    tmp = set()

    for i in range(1, num):
        tmp.add(find(i))

    print(ans if len(tmp) == 1 else -1)

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
    input = sys.stdin.readline #io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
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