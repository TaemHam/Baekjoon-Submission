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

    N, M, K = map(int, input().split())
    L = N+1                                             # 격자 바깥을 판별하기 위해 s2d2 배열에 꼼수를 씀
    mov = (-1, -1-L, -L, -L+1, 1, 1+L, L, L-1)          # 2 3 2 3 2 0 <- 나무가 번식할 좌표에서 s2d2[좌표] 가 0이 나오면
    s2d2 = [0] * L*L                                    # 2 3 2 3 2 0    격자 바깥이라는 의미, 나무를 번식시키지 않음
    nutr = [5] * N*L                                    # 2 3 2 3 2 0 
    land = [dict() for _ in range(N*L)]                 # 2 3 2 3 2 0
    for y in range(0, N*L, L):                          # 2 3 2 3 2 0
        s2d2[y:y+N] = map(int, input().split())         # 0 0 0 0 0 0

    for _ in range(M):
        x, y, z = map(int, input().split())
        land[(x-1)*L+(y-1)][z] = 1
    
    for _ in range(K):

        '''봄, 여름 페이즈'''
        for xy in range(N*L):

            if land[xy]:
                dead = 0
                alive = dict()
                nutri = nutr[xy]

                for age in sorted(land[xy].keys()):
                    trees = land[xy][age]
                    if nutri >= age * trees:
                        alive[age + 1] = trees
                        nutri -= age * trees
                    else:
                        survived = nutri // age
                        if survived:
                            alive[age + 1] = survived
                            nutri -= age * survived
                        dead += age // 2 * (trees - survived)

                land[xy] = alive
                nutr[xy] = nutri + dead

        '''가을, 겨울 페이즈'''
        for xy in range(N*L):

            if s2d2[xy]:
                for age in land[xy]:
                    if not age % 5:
                        for d in mov:
                            if s2d2[xy+d]:
                                if 1 in land[xy+d]:
                                    land[xy+d][1] += land[xy][age]
                                else:
                                    land[xy+d][1] = land[xy][age]
                                    
                nutr[xy] += s2d2[xy]

    print(sum(sum(land[xy].values()) for xy in range(N*L)))

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