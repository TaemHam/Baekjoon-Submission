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

    input = sys.stdin.readline
    tarn = int(input().strip())
    targ = list(map(int,list(str(tarn))))
    n = int(input())
    t_ans = abs(tarn - 100)                     # 무지성으로 돌리기만 해서 찾을 때 누르는 횟수

    if n == 10:                                 # 다 망가졌으면 위아래로 돌리면 됨
        print(t_ans)
        return

    brok = set(map(int,input().split()))
    smld = [9,1,8,2,7,3,6,4,5]
    bigd = [1,9,2,8,3,7,4,6,5]
    vssd = [1,-1,2,-2,3,-3,4,-4,5,-5,6,-6,7,-7,8,-8,9,-9]
    vsbd = [-i for i in vssd]

    for i in range(len(targ)):
        if targ[i] not in brok:                 # 채널 왼쪽 숫자부터 차례대로 안망가졌으면 넘어감
            continue

        else:                                   # 망가진 숫자 찾음
            if i < len(targ)-1:
                if targ[i+1] >= 5:              # 다음 숫자가 5보다 작으면 빼는게, 크면 더하는게 가까움
                    a = bigd
                else:
                    a = smld
            else: a = smld                      # 마지막 숫자는 상관 없음

            if i == 0 and targ[i] == 5:         # 절반 엣지 케이스
                a = [a[-1]] + a[:-1]

            if len(targ) == 1:                  # 채널이 10 미만일 때 마이너스 채널 방지용
                if targ[i] >= 5:
                    a = vsbd
                else:
                    a = vssd

            for j in range(len(a)):             # 위아래로 탐색하며 가장 가까운 안망가진 숫자 탐색

                if len(targ) == 1:              # 마이너스 채널 방지용
                    b = targ[i] + a[j]
                    if b < 0:
                        continue
                    elif b >= 10:
                        b %= 10
                    if b in brok:
                        continue

                else: 
                    b = (targ[i] + a[j]) % 10
                if b in brok and (i != 0 or b != 0):
                    continue

                else:                               # 가장 가까운 안망가진 숫자 찾음
                    c = False
                    if a[j] <= 4:                   # 더해야 하는 경우 10이 넘어가면 1을 올림
                        if targ[i] + a[j] >= 10:
                            if i == 0:              # 첫 숫자라면 왼쪽에 1을 더할 준비
                                c = 1
                            else:                   # 아니라면 전 숫자에 1을 더할 준비
                                c = targ[i-1] + 1
                            if c in brok:           # 더한 숫자도 망가졌으면 다시 탐색
                                continue
                    elif a[j] >= 6:                 # 빼야 하는 경우 0보다 낮으면 1을 내림
                        if targ[i] + a[j] <= 10:
                            if i == 0:              # 첫 숫자라면 왼쪽 숫자 뺄 준비
                                c = 'd'
                            else:                   # 아니라면 전 숫자에 1을 뺄 준비
                                c = targ[i-1] - 1
                            if c in brok and i != 0:# 뺀 숫자도 망가졌으면 다시 탐색
                                continue            # 첫 숫자가 0이면 입력 할 필요가 없는 엣지 케이스

                    targ[i] = b                     # 찾은 숫자 변경 후 뒷 숫자들도 바꿔야 함
                    if i != len(targ)-1:            # 마지막 숫자는 뒷숫자가 없으므로 스킵
                        if a[j] <= 4:               # 더한 경우 채널을 내려 탐색해야 하니 0으로
                            d = 0
                            while d in brok:        # 망가진 숫자라면 재탐색
                                d += 1
                        else:                       # 뺀 경우 올려 탐색해야 하니 9로
                            d = 9
                            while d in brok:        # 역시 재탐색
                                d -= 1

                        for k in range(i+1,len(targ)):
                            targ[k] = d             # 뒷 숫자 변경 완료

                break                               # j 빼고
        if c != False:
            if i == 0 and c == 'd':                 # i 빼기 전 앞 숫자도 변경
                targ = targ[1:]
                if len(targ) == 0:
                    targ.append(0)
            elif i == 0:
                targ = [1] + targ
            else:
                targ[i-1] = c
        break                                       # i 빼기
    print(targ)
    
    t_ans2 = len(targ)                              # 숫자 버튼 누르는 횟수 더하기
    t_ans2 += abs(tarn - int(''.join(map(str,targ))))    # 채널 돌려야 하는 횟수

    print(min(t_ans,t_ans2))                        # 무지성 돌리기랑 채널 누르고 돌리기 비교


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
    input = sys.stdin.readline  # by default
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