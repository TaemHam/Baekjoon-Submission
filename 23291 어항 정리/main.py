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

    # 어려웠던 점:
    # 두 번째 공중 부양할 때 쌓을 위치의 인덱스 찾는 게 계속 헷갈려서 시간이 걸림


    # 첫 번째 공중 부양을 위한 sav 배열 만드는 과정    
    # hnw = [1, 0]
    # arr = []
    # cur = 0
    # for i in range(3, 22):
    #    nxt = cur + i//2
    #    nhnw = hnw[:]
    #    while len(arr) < nxt:
    #        arr.append([len(arr) - cur] + nhnw))
    #    hnw[i%2] += 1
    #    cur = nxt
    # sav = arr[3:100:4]

    # 인접한 칸 물고기 차이 구해서 옮기는 함수
    def organize(a, b):
        val = int((brd[b] - brd[a])/5)
        dif[a] += val
        dif[b] -= val

    N, K = map(int, input().split())
    sav = [[], 
        [0, 2, 1], [2, 2, 2], [0, 3, 3], [0, 4, 3], [0, 4, 4], 
        [4, 4, 4], [3, 5, 4], [2, 5, 5], [0, 6, 5], [4, 6, 5], 
        [2, 6, 6], [6, 6, 6], [3, 7, 6], [0, 7, 7], [4, 7, 7], 
        [0, 8, 7], [4, 8, 7], [0, 8, 8], [4, 8, 8], [8, 8, 8], 
        [3, 9, 8], [7, 9, 8], [2, 9, 9], [6, 9, 9], [0, 10, 9]]
    tail, wdt, hgt = sav[N//4]
    lim = N * max(hgt+1, 4)
    brd = [0] * lim
    brd[:N] = list(map(int, input().split()))

    for cnt in range(100):
        M = max(brd[:N])
        m = min(brd[:N])
        if M-m <= K:
            break

        '''물고기 추가'''
        for i in range(N):
            if brd[i] == m:
                brd[i] += 1

        '''첫 번째 공중 부양'''
        dir = 1
        flt, cur = N-tail, N-tail
        for i in range(wdt):
            for _ in range(wdt-i):
                flt -= 1
                cur -= 1 * dir
                brd[flt], brd[cur] = brd[cur], brd[flt]
            for _ in range(hgt-i):
                flt -= 1
                cur += N * dir
                brd[flt], brd[cur] = brd[cur], brd[flt]
            dir *= -1
        
        '''첫 번째 수량 조절'''
        dif = [0] * lim
            # 꼬리 정리
        for loc in range(N-tail, N):
            organize(loc, loc-1)
            # 몸통 가로 정리
        for std in range(N-tail-wdt, N*(hgt+1), N):
            for loc in range(std, std+wdt-1):
                organize(loc, loc+1)
            # 몸통 세로 정리
        for std in range(N-tail-wdt, N*hgt, N):
            for loc in range(std, std+wdt):
                organize(loc, loc+N)
            # 결과 더하기
        for std in range(N-tail-wdt, N*(hgt+1), N):
            for loc in range(std, std+wdt):
                brd[loc] += dif[loc]
        for loc in range(N-tail, N):
                brd[loc] += dif[loc]

        '''첫 번째 일렬 정리'''
        flt = 0
        for std in range(N-tail-wdt, N-tail):
            for loc in range(std, N*(hgt+1), N):
                brd[loc], brd[flt] = brd[flt], brd[loc]
                flt += 1

        '''두 번째 공중 부양'''
        lvl = 2*N-1
        for loc in range(N//2):
            brd[loc], brd[lvl-loc] = brd[lvl-loc], brd[loc]

        lvl = 4*N + N//2 - 1
        for std in range(N//2, 2*N, N):
            for loc in range(std, N//4 + std):
                brd[loc], brd[lvl-loc] = brd[lvl-loc], brd[loc]

        '''두 번째 수량 조절'''
        dif = [0] * lim
            # 가로 정리
        for std in range(N-N//4, N*4, N):
            for loc in range(std, std+N//4 - 1):
                organize(loc, loc+1)
            # 세로 정리
        for std in range(N-N//4, N*3, N):
            for loc in range(std, std+N//4):
                organize(loc, loc+N)
            # 결과 더하기
        for std in range(N-N//4, N*4, N):
            for loc in range(std, std+N//4):
                brd[loc] += dif[loc]

        '''두 번째 일렬 정리'''
        flt = 0
        for std in range(N-N//4, N):
            for loc in range(std, N*4, N):
                brd[loc], brd[flt] = brd[flt], brd[loc]
                flt += 1
    
    print(cnt)
                    
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