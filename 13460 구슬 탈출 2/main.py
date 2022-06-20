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
#from bisect import insort_left as il
DEBUG = False


def main(f=None):
    init(f)
    # ######## INPUT AREA BEGIN ##########

    N, M = map(int, input().split())
    NM = N*M
    cur = 0 # 구슬 좌표
    tgt = 0 # 구멍 좌표                 
    mov = [[0] * NM for _ in range(4)]          # mov에는 각 위치에서 기울였을 때 움직이는 칸 수를 저장
    mov_y = [M] * M                             # 0이 위, 1이 아래, 2가 왼쪽, 3이 오른쪽

    input()                             
    for y in range(M, NM, M):                   #   #######  /  0   0   0   0   0   0   0  <- 벽이 있는 줄
        tmp = input().strip()                   #   #.....#  /  0   0   0   0   0   0   0  <- 위로 0칸 움직일 수 있음
        mov_x = 1                               #   #.....#  /  0  -7  -7  -7  -7  -7   0  <- 위로 1칸 (= M만큼)
        for x in range(1, M):                   #   #..#..#  /  0 -14 -14   0 -14 -14   0  <- 가운데 벽 제외 위로 2칸
                                                #   #.....#  /  0 -21 -21   0 -21 -21   0
            if tmp[x] == '#':                   #   #.....#  /  0 -28 -28  -7 -28 -28   0
                for i in range(mov_y[x], y, M): #   #######  /  0   0   0   0   0   0   0
                    mov[1][x+i] = y - M - i     #     원본   /           mov[0]
                for i in range(mov_x, x):
                    mov[3][y+i] = x - 1 - i
                mov_y[x] = y + M
                mov_x = x + 1
                continue
            mov[0][y+x] = mov_y[x] - y
            mov[2][y+x] = mov_x - x

            if tmp[x] == 'R':
                cur += y + x
            elif tmp[x] == 'B':
                cur += (y + x) * NM
            elif tmp[x] == 'O':
                tgt += y + x

    bak = (M, -M, 1, -1)    #       |  d%2 == 1  |  d%2 == 0    
    ans = -1                # ------|------------|------------  
    vis = [0] * NM*NM       # a < b |      1     |      0       check는 
    vis[cur] = 1            # ------|------------|------------  구슬 겹치는지 + 구멍에 빠졌는지
    cque = [cur]            # a > b |      0     |      1       확인하기 위한 XOR 함수
    check = lambda d, a, b: (1 if a < b else 0) if d%2 else (0 if a < b else 1)

    for t in range(1, 11):

        nque = []

        for cur in cque:
            Bcur, Rcur = divmod(cur, NM)

            for dir in range(4):
                Bnxt = Bcur + mov[dir][Bcur]
                Rnxt = Rcur + mov[dir][Rcur]

                # 파란 구슬이 빠지는 경우
                if Bnxt == tgt + mov[dir][tgt]:
                    if check(dir, Bcur, tgt):
                        continue

                # 빨간 구슬이 빠지는 경우
                if Rnxt == tgt + mov[dir][tgt]:
                    if check(dir, Rcur, tgt):
                        ans = t
                        cque.clear()
                        nque = []
                        break

                # 구슬 위치가 겹치는 경우
                if Bnxt == Rnxt:
                    Rnxt += bak[dir]
                    if check(dir, Bcur, Rcur):
                        Rnxt, Bnxt = Bnxt, Rnxt

                # 방문한 위치에 있는 경우
                if vis[Bnxt * NM + Rnxt]:
                    continue
                
                # 다음 큐에 추가
                vis[Bnxt * NM + Rnxt] = 1
                nque.append(Bnxt * NM + Rnxt)
            
        if not nque:
            break
        cque = nque
    
    print(ans)

    ######## INPUT AREA END ############


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