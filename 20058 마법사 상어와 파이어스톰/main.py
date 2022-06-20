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
#from heapq import heappush, heapreplace
#import bisect
#from bisect import bisect_left as bl, bisect_right as br
DEBUG = False


def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    N, _ = map(int, input().split())
    N = 2**N
    M = N+1
    dir = [1, -1, M, -M]
    brd = [0] * M*M
    for y in range(0, N*M, M):
        brd[y:y+N] = list(map(int, input().split()))
    
    for L in map(int, input().split()):

        '''돌리기 페이즈'''                              # 아래는 L==2 일 경우의 그림
        if L:                                           # 같은 숫자끼리 시계 방향으로 스왑
            for y in range(0, N*M, M*2**L):             # 1 2 3 1
                for xy in range(y, y+N, 2**L):          # 3 4 4 2 
                    for lvl in range(2**(L-1)):         # 2 4 4 3
                        k = 2**L-1-2*lvl                # 1 3 2 1
                        s = xy+(M+1)*lvl
                        for dst in range(k):
                            brd[s+dst], brd[s+k+dst*M], brd[s+k+k*M-dst], brd[s+k*M-dst*M] = brd[s+k*M-dst*M], brd[s+dst], brd[s+k+dst*M], brd[s+k+k*M-dst]

        '''녹이기 페이즈'''
        mlt = []
        for y in range(0, N*M, M):
            for xy in range(y, y+N):
                if not brd[xy]:
                    continue
                cnt = 0
                for d in dir:
                    if brd[xy+d]:
                        cnt += 1
                if cnt < 3:
                    mlt.append(xy)
        for xy in mlt:
            brd[xy] -= 1
    
    cnt = 0
    vis = [0] * N*M
    for y in range(0, N*M, M):
        for xy in range(y, y+N):
            if brd[xy] and not vis[xy]:
                vis[xy] = 1
                que = [xy]
                for crd in que:
                    for d in dir:
                        if brd[crd+d] and not vis[crd+d]:
                            vis[crd+d] = 1
                            que.append(crd+d)
                cnt = max(cnt, len(que))

    print(str(sum(brd)) + '\n' + str(cnt))
    
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