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
    # 처음에는 지난주 정우씨 쓰셨던 리스트에 함수 저장해서 불러와서 실행시키는 방법을 감명 깊게 봐서 따라해봤는데 틀려서
    # 다시 직접 스왑해주는 방법을 썼는데, 그래도 틀려서 한참을 디버깅해보니 게임판 1차원 배열로 바꾸는 방법이 잘못됐었다...
    # 익숙한 코드라도 짜면 바로바로 확인하는 습관을 길러야겠다.

    N, M, K = map(int, input().split())
    L = M + 1
    mov = [1, L, -1, -L]
    ans = 0
    brd = [0] * N*L
    scr = [0] * N*L
    oob = [0] * N*L + [1] * L
    for y in range(0, N*L, L):
        brd[y:y+M] = list(map(int, input().split()))
        oob[y+M] = 1
        
    cur, dir = 0, 0
    top, bak, rgt, lft, frt, bot = 1, 2, 3, 4, 5, 6
    
    for _ in range(K):
        # 같은 방향으로 움직였을 때 밖으로 나간다면, 방향을 뒤로 돌려줌
        if oob[cur + mov[dir]]:
            dir += 2
            dir %= 4
        
        cur += mov[dir]

        # 점수 배열(scr)에 게임판 크기만큼 0을 초기화 시키고, 주사위가 방문했을때 해당 점수 배열 칸이 0이라면
        # 그 때 BFS 돌려서 연결된 숫자들 위치 찾아 점수 배열에 넣고, 다 찾으면 저장해둔 위치 다시 돌아서 그 갯수를 곱해줌
        if not scr[cur]:
            que = [cur]
            scr[cur] = brd[cur]
            for loc in que:
                for i in range(4):
                    if oob[loc+mov[i]] or scr[loc+mov[i]] or brd[loc+mov[i]] != brd[cur]:
                        continue
                    scr[loc+mov[i]] = brd[cur]
                    que.append(loc+mov[i])

            for loc in que:
                scr[loc] *= len(que)

        ans += scr[cur]

        if dir == 0:
            top, lft, bot, rgt = lft, bot, rgt, top
        elif dir == 2:
            top, lft, bot, rgt = rgt, top, lft, bot
        elif dir == 1:
            top, frt, bot, bak = bak, top, frt, bot
        else:
            top, frt, bot, bak = frt, bot, bak, top

        if bot > brd[cur]:
            dir += 1
            dir %= 4
        elif bot < brd[cur]:
            dir += 3
            dir %= 4

    print(ans)

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