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
    N *= 10
    cur = 0
    tgt = 0
    mov = [[0] * N for _ in range(4)]
    mov_y = [10] * M

    input()
    for y in range(10, N, 10):
        tmp = input().strip()
        mov_x = 1
        for x in range(1, M):

            if tmp[x] == '#':
                for i in range(mov_y[x], y, 10):
                    mov[1][x+i] = y - 10 - i
                for i in range(mov_x, x):
                    mov[3][y+i] = x - 1 - i
                mov_y[x] = y + 10
                mov_x = x + 1
                continue

            if tmp[x] == 'R':
                cur += y + x
            elif tmp[x] == 'B':
                cur += (y + x) * 100
            elif tmp[x] == 'O':
                tgt += y + x

            mov[0][y+x] = mov_y[x] - y
            mov[2][y+x] = mov_x - x

    bak = [10, -10, 1, -1]
    ans = -1
    cnt = 1
    vis = set()
    vis.add(cur)
    cque = [cur]
    nque = []
    check = lambda d, a, b: (1 if a < b else 0) if d % 2 else (0 if a < b else 1)

    while cque:

        while cque:
            Bcur, Rcur = divmod(cque.pop(), 100)

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
                        ans = cnt
                        cque.clear()
                        nque.clear()
                        break

                # 구슬 위치가 겹치는 경우
                if Bnxt == Rnxt:
                    Rnxt += bak[dir]
                    if check(dir, Bcur, Rcur):
                        Rnxt, Bnxt = Bnxt, Rnxt

                # 방문한 위치에 있는 경우
                if Bnxt * 100 + Rnxt in vis:
                    continue
                
                # 다음 큐에 추가
                vis.add(Bnxt * 100 + Rnxt)
                nque.append(Bnxt * 100 + Rnxt)
            
        if not nque:
            break
        cque, nque = nque, cque
        cnt += 1
    
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