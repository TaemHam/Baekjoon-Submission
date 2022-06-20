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

    # 접근 방법:
    #   1. 게임판을 1차원 배열로 만들어 뱀 몸통은 1로, 사과는 2로 저장
    #   2. 머리 위치와 방향, 꼬리 위치와 방향을 따로 저장해서, 머리가 빈 칸에 도착하면 꼬리 칸과 스왑해주는 방식을 사용
    #   3. 몸통 길이를 갱신해주면서 꼬리도 머리의 이동 정보(cmd)를 따라가도록 함 (몸통 길이가 3이고 머리가 10초후에 꺾으면 꼬리는 13초 후에 꺾음)

    # 어려웠던 점:
    #   1. 처음에는 꼬리 방향 갱신을 머리 방향 갱신할 때랑 같이 했는데, 그렇게 하니 사과를 먹을 때 꼬리 방향이 한 번 더 꺾여버려 오류가 났었다.
    #   2. 1차원 배열 한 줄을 원래 100칸으로 썼는데, N이 100일 때 게임판 밖으로 나가는지 체크하는 배열(oob)이 망가져 또 오류가 났었다.

    dd = [1, 101, -1, -101]
    ds = {'D': 1, 'L': -1}
    N = int(input().strip())
    head, tail = 0, 0       # 머리, 꼬리 좌표
    hdir, tdir = 0, 0       # 머리, 꼬리 방향
    len = 1                 # 몸통 길이
    cmd = [0] * 10000       # 이동 정보
    brd = [0] * N*101 
    brd[0] = 1
    ans = 10000
    oob = [0] * N*102
    for i in range(0, 101*N, 101):
        oob[i:i+N] = [1] * N

    for _ in range(int(input().strip())):
        y, x = map(lambda x: int(x)-1, input().split())
        brd[101*y + x] = 2
    
    for _ in range(int(input().strip())):
        t, s = input().split()
        cmd[int(t)] = ds[s]

    for t in range(1, 10000):

        head += dd[hdir]
        if oob[head] and brd[head] != 1:

            if not brd[head]:   # 빈 칸
                brd[head], brd[tail] = 1, 0
                tdir += cmd[t-len]
                tdir %= 4
                tail += dd[tdir]

            else:               # 사과
                brd[head] -= 1
                len += 1

        else:   # 몸통이나 벽
            ans = t
            break

        hdir += cmd[t]
        hdir %= 4

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