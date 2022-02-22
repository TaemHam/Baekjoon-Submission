# CP template Version 1.006
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
#from itertools import product
#import collections
#from collections import deque
#from collections import defaultdict as dd
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

    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    N, M, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    nutr = [[5] * N for _ in range(N)]
    land = [[dict() for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        x, y, z = map(int, input().split())
        land[x-1][y-1][z] = 1
    
    for _ in range(K):

        for y in range(N):
            for x in range(N):
                if land[y][x]:
                    dead = 0
                    alive = dict()
                    nutri = nutr[y][x]

                    for age in sorted(land[y][x].keys()):
                        trees = land[y][x][age]
                        if nutri >= age * trees:
                            alive[age + 1] = trees
                            nutri -= age * trees
                        else:
                            survived = nutri // age
                            if survived:
                                alive[age + 1] = survived
                                nutri -= age * survived
                            dead += age // 2 * (trees - survived)

                    nutr[y][x] = nutri + dead
                    land[y][x] = alive

        for y in range(N):
            for x in range(N):
                nutr[y][x] += A[y][x]

                for age in land[y][x]:
                    if not age % 5:
                        for i in range(8):
                            ny = y + dy[i]
                            nx = x + dx[i]
                            if 0 <= ny < N and 0 <= nx < N:
                                if 1 in land[ny][nx]:
                                    land[ny][nx][1] += land[y][x][age]
                                else:
                                    land[ny][nx][1] = land[y][x][age]
    answer = 0
    for y in range(N):
        for x in range(N):
            for age in land[y][x]:
                answer += land[y][x][age]

    print(answer)

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