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
    dy = [0, -1, 1, 0, 0]
    dx = [0, 0, 0, -1, 1]
    N, M, K = map(int, input().split())
    remove_list = set()
    remaining = set(range(1, M+1))
    shark = [[] for _ in range(M+1)]
    smell = [[0] * N for _ in range(N)]
    trail = set()
    mov = [[tuple()] for _ in range(M+1)]
    brd = []
    for y in range(N):
        tmp = list(map(int, input().split()))
        for x in range(N):
            if tmp[x]:
                shark[tmp[x]] = [y, x]
                smell[y][x] = K
                trail.add((y, x))
        brd.append(tmp)
    
    
    dir = [0] + list(map(int, input().split()))
    for i in range(1, M+1):
        shark[i].append(dir[i])
        for _ in range(4):
            mov[i].append(tuple(map(int, input().split())))
    

    for sec in range(1, 1001):

        # 이동 페이즈
        for ith_shk in remaining:
            y, x, d = shark[ith_shk]
            cnd = []

            for i in range(4):
                nd = mov[ith_shk][d][i]
                ny = y + dy[nd]
                nx = x + dx[nd]
                if 0 <= ny < N and 0 <= nx < N:
                    if not brd[ny][nx]:
                        shark[ith_shk] = [ny, nx, nd]
                        break
                    elif brd[ny][nx] == ith_shk and not cnd:
                        cnd = [ny, nx, nd]
            else:
                shark[ith_shk] = cnd
        

        # 냄새 삭제 페이즈
        for y, x in trail:
            smell[y][x] -= 1
            if not smell[y][x]:
                brd[y][x] = 0
                remove_list.add((y, x))
        while remove_list:
            trail.discard(remove_list.pop())


        # 빤스런, 냄새 갱신 페이즈
        for ith_shk in remaining:
            y, x, _ = shark[ith_shk]

            if not brd[y][x]:
                brd[y][x] = ith_shk
                smell[y][x] = K
                trail.add((y, x))
            else:
                if brd[y][x] == ith_shk:
                    smell[y][x] = K
                else:
                    remove_list.add(ith_shk)
        while remove_list:
            remaining.discard(remove_list.pop())

        # 정답 체크 페이즈
        if len(remaining) == 1:
            print(sec)
            break
    
    else:
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