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
#from heapq import heappush, heappop, heapreplace
#import bisect
#from bisect import insort_left as il
DEBUG = False


def main(f=None):
    init(f)
    # ######## INPUT AREA BEGIN ##########

    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    N = int(input().strip())
    f1, f2 = 1, 1
    brd = []
    trn = [[1] * N for _ in range(N)]
    mov = [[[1] * N for _ in range(N)] for _ in range(2)]
    vis = [[[0] * N for _ in range(N)] for _ in range(2)]
    oob = [[[0] * (N+1) for _ in range(N+1)] for _ in range(2)]
    oob[0][0], oob[0][N-1], oob[0][N], oob[1][N] = [[1] * (N+1) for _ in range(4)]

    for y in range(N):
        oob[1][y][0], oob[1][y][N-1], oob[1][y][N], oob[0][y][N] = [1] * 4
        tmp = input().strip()
        for x in range(N):
# 0 세로 / 1 가로
            if tmp[x] == 'B':
                if not f1:
                    BBB = (1 if tmp[x-1] == 'B' else 0, y, x)
                f1 -= 1

            elif tmp[x] == 'E':
                if not f2:
                    EEE = (1 if tmp[x-1] == 'E' else 0, y, x)
                f2 -= 1
            
            elif tmp[x] == '1':
                l, r, u, d = max(0, x-1), min(N, x+2), max(0, y-1), min(N, y+2)
                mov[1][y][l:r] = [0] * (r-l)
                for i in range(u, d):
                    trn[i][l:r] = [0] * (r-l)
                    mov[0][i][x] = 0

        brd.append(tmp)
    
    cque = [BBB]
    nque = []
    cnt = 0
    ans = 0

    while cque:

        while cque:
            d, y, x = cque.pop()

            if (d, y, x) == EEE:
                ans = cnt
                nque.clear()
                break

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if oob[d][ny][nx] or vis[d][ny][nx] or not mov[d][ny][nx]:
                    continue

                vis[d][ny][nx] = 1
                nque.append((d, ny, nx))
            
            if oob[0][x][y] or oob[1][x][y] or vis[1-d][y][x] or not trn[y][x]:
                continue

            vis[1-d][y][x] = 1
            nque.append((1-d, y, x))

        cnt += 1
        cque, nque = nque, cque

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