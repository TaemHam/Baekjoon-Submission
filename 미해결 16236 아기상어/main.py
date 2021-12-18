# CP template Version 1.006
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
#from itertools import product
#import collections
from collections import deque
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

    n = int(input())
    mat = []
    for y in range(n):
        l = input().split()
        for x in range(n):
            if l[x] == '9':
                loc = (x, y)
                l[x] = '0'
        mat.append(l)                                           # 맵을 mat에 저장하면서 아기상어의 위치는 '0'으로 바꿔줌;
    
    dx = [0,-1,1,0]
    dy = [-1,0,0,1]
    stomach = 0                                                 # stomach랑 size는 '사이즈와 같은 수의 물고기를 먹으면 사이즈 업!'
    size = 2                                                    # 을 구현하기 위해 씀;

    edible = set(['1'])                                         # 현재 상어 사이즈보다 작은 물고기들 edible에 저장;
    
    turn_total = 0                                              # 움직임 수 총합(정답제출용)은 turn_total에 저장;

    while True:                                                 # 물고기 한 번 먹을 때마다 이리로 돌아옴;

        q = deque([loc])                                        # q는 bsf에 쓰일 더블엔드큐로 좌표형태로 저장;

        v = set()                                               # 방문한 좌표(v)는 set에 넣어서 빠르게 확인;

        breadth = len(q)                                    ##### breadth 랑 turn 은 같은 거리에 있는 모든 칸 확인하려고 넣었음;
        turn = 0                                            ##### 각 BSF 단계에서 큐를 다 쓸 때마다 거리(turn)를 +1 하는 걸로 구현했음;

        menu = []                                               # menu는 가장 가까운 거리에 있는 모든 물고기들 중에
                                                                # 가장 위에 있는 물고기를 먹어야 해서 그거 sort 하려고 넣음;
        while q: 
            x,y = q.popleft()
            v.add((x, y))
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]                    # 밑줄 edible에 union 한 이유는 같은 사이즈 물고기를 먹진 못해도 지나다닐 수 있어서;
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in v and mat[ny][nx] in edible.union('0', str(size)):
                    if mat[ny][nx] in edible:
                        menu.append((nx,ny))                    # 먹을 수 있는 물고기 찾으면 menu에 넣어서 
                    q.append((nx, ny))                          # 같은 거리에 있는 다른 물고기도 넣어줌;

            breadth -= 1
            if breadth == 0:                                    # 같은 거리에 있는 칸을 모두 확인 했을 때 
                turn += 1                                       # menu 도 확인해서 먹을 물고기 정해줌;
                breadth = len(q)
                if menu:
                    x,y = min(menu, key = lambda x : (x[1], x[0]))
                    mat[y][x] = '0'                             # 먹은 물고기 '0'으로 바꾸고
                    stomach += 1                                # 뱃속에 들어간 물고기 갯수 카운트 해주고
                    if stomach == size:                         # 물고기 몸집 키우면서 뱃속 물고기 갯수도 0으로 바꿔주고
                        edible.add(str(size))
                        size += 1
                        stomach = 0
                    loc = (x, y)                                # 상어 위치 갱신해주고
                    turn_total += turn                          # 물고기 먹으러 오면서 사용한 시간 누적시켜주고;
                    break

        else:                                                   # 여기서 bsf 한번 더 돌려서 큐를 다 썼는데도 먹을 물고기가 없으면
            break                                               # 다 먹은거니까 while True 탈출해서 total turn 출력해줬음;

    print(turn_total)






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