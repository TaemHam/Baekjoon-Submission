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

    n, m = map(int, input().split())
    grp = []
    for y in range(n):
        t = input().strip()
        if 0 < y < n-1:
            for x in range(1, m-1):
                if t[x] == 'R':
                    red = (y, x)
                elif t[x] == 'B':
                    blu = (y, x)
        grp.append(t)

    dy = [1, -1, 0, 0]          # 아래, 위, 오른쪽, 왼쪽
    dx = [0, 0, 1, -1]

    q = deque()
    q.append((red, blu, -1))
    check, move = 1, 1

    while move <= 10 and q:
        c_r, c_b, p_i = q.popleft()
        if p_i in [0, 1]:
            l, r = 2, 4
        elif p_i in [2, 3]:
            l, r = 0, 2
        else:
            l, r = 0, 4
        check -= 1

        for i in range(l, r):                       #방향 체크 해서 움직일 수 있는지 봄
            dir_y = c_r[0] + dy[i]
            dir_x = c_r[1] + dx[i]
            if (dir_y, dir_x) == c_b:               #파란 구슬이 있으면 그 다음칸 체크
                dir_y += dy[i]
                dir_x += dx[i]

            if grp[dir_y][dir_x] == '#':
                dir_y = c_b[0] + dy[i]
                dir_x = c_b[1] + dx[i]
                if (dir_y, dir_x) == c_r:
                    dir_y += dy[i]
                    dir_x += dx[i]
                if grp[dir_y][dir_x] == '#':
                    continue

            cas = 0
            b_y, b_x = c_b
            while grp[b_y][b_x] != '#':
                b_y += dy[i]
                b_x += dx[i]
                if grp[b_y][b_x] == 'O':
                    cas = 1
                    break
                if (b_y, b_x) == c_r:
                    cas = 2
            if cas == 1:                # 파란 구슬이 골인 하는 경우는 스킵
                continue
            elif cas == 2:              # 빨간 구슬이 경로에 있는 경우 1칸 전에 멈춰야함
                b_y -= dy[i]
                b_x -= dx[i]
            n_b = (b_y - dy[i], b_x - dx[i])

            r_y, r_x = c_r
            while grp[r_y][r_x] != '#':
                r_y += dy[i]
                r_x += dx[i]
                if grp[r_y][r_x] == 'O':
                    cas = 3
                    break
                if (r_y, r_x) == c_b and cas == 0:
                    cas = 4
            if cas == 3:                # 빨간 구슬이 골인 하는 경우는 끝내야함
                print(move)
                return
            elif cas == 4:
                r_y -= dy[i]
                r_x -= dx[i]
            n_r = (r_y - dy[i], r_x - dx[i])

            q.append((n_r, n_b, i))
        if check == 0:
            move += 1
            check = len(q)

    print(-1)








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