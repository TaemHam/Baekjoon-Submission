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

    def grav(brd):
        cur = list(range(20, 24))
        for y in range(20, -1, -4):
            for x in range(4):
                if brd[x+y] == 0:
                    continue
                elif brd[x+y] == 1:
                    brd[x+y], brd[cur[x]] = brd[cur[x]], brd[x+y]
                    cur[x] -= 4
                else: # brd[x+y] == 2:
                    h = min(cur[x], cur[x+1]-1)
                    brd[x+y], brd[h] = brd[h], brd[x+y]
                    cur[x] = h-4
                    cur[x+1] = h+1

    def play1(brd, c): # 단일 블럭
        h = 5
        for xy in range(c, 24, 4):
            if brd[xy]:
                h = xy//4-1
                break
        
        brd[h*4+c] = 1
        flg = 0

        if 0 not in brd[h*4:h*4+4]:
            scr.append(1)
            brd[h*4:h*4+4] = [0] * 4
            flg = 1

        while flg:
            flg = 0
            grav(brd)
            for y in range(20, 7, -4):
                if 0 not in brd[y:y+4]:
                    scr.append(1)
                    brd[y:y+4] = [0] * 4
                    flg = 1

        k = 0
        if [1 for i in brd[4:8] if i]:
            k = 4
        if k:
            brd[:] = [0] * k + brd[:24-k]

    def play2(brd, c): # 가로 블럭
        h = 5
        for x in range(c, c+2):
            for xy in range(x, 24, 4):
                if brd[xy]:
                    h = min(h, xy//4-1)
                    break

        brd[h*4+c] = 2
        brd[h*4+c+1] = 1
        flg = 0

        if 0 not in brd[h*4:h*4+4]:
            scr.append(1)
            brd[h*4:h*4+4] = [0] * 4
            flg = 1

        while flg:
            flg = 0
            grav(brd)
            for y in range(20, 7, -4):
                if 0 not in brd[y:y+4]:
                    scr.append(1)
                    brd[y:y+4] = [0] * 4
                    flg = 1

        k = 0
        if [1 for i in brd[4:8] if i]:
            k = 4
        if k:
            brd[:] = [0] * k + brd[:24-k]

    def play3(brd, c): # 세로 블럭
        h = 5
        for xy in range(c, 24, 4):
            if brd[xy]:
                h = xy//4-1
                break
        
        brd[h*4+c] = 1
        brd[h*4+c-4] = 1
        flg = 0

        for y in range(h*4, h*4-5, -4):
            if 0 not in brd[y:y+4]:
                scr.append(1)
                brd[y:y+4] = [0] * 4
                flg = 1

        while flg:
            flg = 0
            grav(brd)
            for y in range(20, 7, -4):
                if 0 not in brd[y:y+4]:
                    scr.append(1)
                    brd[y:y+4] = [0] * 4
                    flg = 1

        k = 0
        if [1 for i in brd[4:8] if i]:
            k = 4
            if [1 for i in brd[0:4] if i]:
                k = 8
        if k:
            brd[:] = [0] * k + brd[:24-k]

    grn = [0] * 24
    blu = [0] * 24
    scr = []

    for num in range(int(input().strip())):
        t, x, y = map(int, input().split())
        if t == 1:
            play1(grn, y)
            play1(blu, 3-x)
        elif t == 2:
            play2(grn, y)
            play3(blu, 3-x)
        else: # t == 3:
            play3(grn, y)
            play2(blu, 2-x)

        print('초록'+str(num+1)+"번 블럭")
        for y in range(0, 24, 4): # 초록 파랑 보드 확인용
            print(grn[y:y+4])
        print('파랑'+str(num+1)+"번 블럭")
        for y in range(0, 24, 4):
            print(blu[y:y+4])
        print()

    print(str(len(scr)) + '\n' + str(len([1 for i in grn if i]) + len([1 for i in blu if i])))

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