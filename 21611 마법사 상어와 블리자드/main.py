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
    # 처음에는 가운데에서부터 스택에 쌓으면서 쌓고 있던 숫자와 다른 숫자를 만났을 때 갯수만큼 바로바로 폭발시키면서 풀었는데, 
    # 역시나 반례가 있었다(예: 1 1 1 2 2 2 2 1 2 2 2 2 1 1 1 의 경우 마지막 1 3개가 남아서 실패).

    N, M = map(int, input().split())
    # 2차원 격자보다 가운데칸에서부터 쌓아놓은 1차원 스택을 사용
    tmp = []
    for _ in range(N):
        tmp.extend(map(int, input().split()))
    # 블리자드 (blz) 배열에 1차원 스택 사용시 각 방향으로의 마법 사용시 불러와야하는 인덱스를 저장
    # 인덱스가 1, 2, 2, 2, 3, 4, 4, 4 로 늘어나 jmp 배열을 사용해서 저장했음
    jmp = [1, 2, 2, 2]
    loc = 0
    blz = [[] for _ in range(4)]
    for i in range(N//2):
        for d in range(4):
            loc += jmp[d] + 2*i
            blz[d].append(loc)
    # blz 배열을 좌 하 우 상 순서에서 상 하 좌 우 순서로 바꿔줌
    blz = [[]] + [blz[3]] + [blz[1]] + [blz[0]] + [blz[2]]

    # 1차원 스택으로 바꾸는 과정
    # 정 가운데부터 좌로 1칸, 밑으로 1칸, 우로 2칸, 위로 2칸, 다시 좌로 3칸 등으로 움직이는 패턴 구현을 위해 jmp 배열 재사용
    jmp[1] -= 1 
    mov = [-1, N, 1, -N]
    brd = [0]
    loc = N*N // 2
    for i in range(N//2):
        for d in range(4):
            for _ in range(jmp[d]):
                loc += mov[d]
                brd.append(tmp[loc])
            jmp[d] += 2
    # 가장 윗줄이 안들어가서 넣어줌
    brd.extend(tmp[N-2::-1])

    ans = 0
    for _ in range(M):
        D, S = map(int, input().split())
        # 마법 시전 페이즈
        for i in range(S):
            if blz[D][i] >= len(brd):
                break
            brd[blz[D][i]] = 0

        # 구슬 폭발 페이즈
        boom = 1
        while boom:
            boom = 0
            nbrd = [0]
            cnt = 1
            for i in brd[1:]:
                if i:
                    if i == nbrd[-1]:
                        cnt += 1
                    else:
                        if cnt >= 4:
                            boom = 1
                            for _ in range(cnt):
                                ans += nbrd.pop()
                        cnt = 1
                    nbrd.append(i)
            if cnt >= 4:
                boom = 1
                for _ in range(cnt):
                    ans += nbrd.pop()
            brd = nbrd

        # 갯수 표현 페이즈
        # 스택에 마지막에 쌓여있는 구슬 번호가 다음 구슬 번호와 다르면 구슬 갯수 (1) 구슬 번호 스택에 쌓고, 같다면 갯수를 올려줌
        nbrd = [0]
        for i in brd[1:]:
            if i == nbrd[-1]:
                nbrd[-2] += 1
            else:
                if len(nbrd) == N*N:
                    break
                nbrd.append(1)
                nbrd.append(i)
        brd = nbrd

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