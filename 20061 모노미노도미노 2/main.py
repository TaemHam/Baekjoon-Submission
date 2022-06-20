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
#from bisect import bisect_left as bl
DEBUG = False


def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    def play(brd, blk, col): # brd는 보드 종류, blk은 블럭 종류, col은 떨어지는 위치

        '''높이 확인 페이즈'''
        h = 0
        for xy in range(20+col, -1, -4):
            if brd & 1<<xy:
                h = xy//4+1
                break
        if blk == 2: # 가로 블럭은 오른쪽 줄도 확인
            for xy in range(21+col, -1, -4):
                if brd & 1<<xy:
                    h = max(h, xy//4+1)
                    break
        
        '''블럭 추가 페이즈'''
        loc = h<<2
        brd |= 1 << loc+col

        if blk == 2: # 가로 블럭은 오른쪽도 추가
            brd |= 1 << loc+col+1
            
        elif blk == 3: # 세로 블럭은 위쪽도 추가
            brd |= 1 << loc+col+4
            
            '''점수 라인 제거 페이즈'''
            if not ~brd & 15 << loc+4:
                scr.append(1)
                brd = (brd & (1 << loc+4)-1) | (brd>>4 & ~((1 << loc+4)-1))

        if not ~brd & 15 << loc:
            scr.append(1)
            brd = (brd & (1 << loc)-1) | (brd>>4 & ~((1 << loc)-1))

        '''돌출 부분 정리 페이즈'''
        if brd & 15 << 16:
            brd >>= 4
            if brd & 15 << 16:
                brd >>= 4
        
        return brd

    grn = blu = 0
    swp = (0, 1, 3, 2)
    scr = []

    for _ in range(int(input().strip())):
        t, x, y = map(int, input().split())
        grn = play(grn, t, y)
        blu = play(blu, swp[t], x)
    
    # for y in range(20, -1, -4): # 초록 파랑 보드 확인용
    #     for xy in range(y, y+4):
    #         print(1 if grn & 1<<xy else 0, end=' ')
    #     print()
    # print('위 초록 아래 파랑')
    # for y in range(20, -1, -4):
    #     for xy in range(y+3, y-1, -1):
    #         print(1 if blu & 1<<xy else 0, end= ' ')
    #     print()
    # print()

    cnt = 0
    while grn:
        grn &= grn-1
        cnt += 1
    while blu:
        blu &= blu-1
        cnt += 1

    print(str(len(scr)) + '\n' + str(cnt))

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