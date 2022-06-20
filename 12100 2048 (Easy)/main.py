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

    # 접근 방법:
    #   1. 게임판을 1차원 배열로 저장 후, bfs를 통해 4가지 방향으로 움직였을 때(mov 함수)의 보드를 복사해 시뮬레이션 실행
    #   2. 세로로 이동하는 경우는 세로를 기준으로, 가로는 가로를 기준으로, 각 줄마다 빈 칸을 제외한 블럭 정보를 빼옴 (get 함수)
    #   3. 이동 방향 끝칸부터 역으로 채워나가며 공백이면 넣고, 같은 블럭이면 합치고, 다른 블럭이면 다음칸에 넣음 (mrg 함수)
    #   4. 5회 이동이 끝나면 다음 큐에 넣어놓은 보드들의 블럭 중 가장 큰 수의 블럭을 출력

    # 어려웠던 점:
    #   1. 같은 블럭이면 합치고 다음 빈칸으로 넘겨줬어야 하는데, 계속 합치게 둬서 (2 2 4 8 같은 경우) 4%에서 많이 틀렸다
    #   2. 문제를 풀고 나서 코드를 좀 더 빠르게 돌리기 위해, 방문 set을 만들어서 게임판 전체를 저장해두고, 같은 판이 나오면 스킵해서 pruning 했었는데,
    #      왠지 모르겠지만 어떻게 바꿔도 실패했다. 이유는 아직도 모르겠음.

    def get(cur):
        if brd[cur]:
            que.append(brd[cur])
            brd[cur] = 0

    def mrg(cur, dir):
        for val in que:
            if brd[cur] == 0:
                brd[cur] = val
            elif brd[cur] == val:
                brd[cur] = val * 2
                cur += dir
            else: #brd[cur] != val:
                cur += dir
                brd[cur] = val
        que.clear()
            
    def mov(dir):
        if dir == 0:
            for x in range(0, N, 1):
                for y in range(0, M, N):
                    get(y+x)
                mrg(x, N)
        elif dir == 1:
            for x in range(0, N, 1):
                for y in range(M-N, -N, -N):
                    get(y+x)
                mrg(M-N+x, -N)
        elif dir == 2:
            for y in range(0, M, N):
                for x in range(0, N, 1):
                    get(y+x)
                mrg(y, 1)
        else: #dir == 3:
            for y in range(0, M, N):
                for x in range(N-1, -1, -1):
                    get(y+x)
                mrg(y+N-1, -1)

    N = int(input().strip())
    M = N*N
    brd = []
    for _ in range(N):
        brd += list(map(int, input().split()))
    que = []
    cque = [brd]
    nque = []

    for _ in range(5):

        while cque:
            pbrd = cque.pop()
            for dir in range(4):
                brd = pbrd[:]
                mov(dir)
                nque.append(brd)

        cque, nque = nque, cque

    print(max(max(i) for i in cque))


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