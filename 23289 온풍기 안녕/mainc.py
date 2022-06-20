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
    from collections import deque

    # 우 좌 상 하
    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]



    def process(temp, lst_heater, wall, lst_ins, R, C, K):
        #온풍기들을 각각 실행하는 부분    
        for i, j, dr in lst_heater:
            #한 온풍기에서 나온 바람은 중복되지 않음
            visited = [[False for _ in range(C)] for _ in range(R)]
            ts = deque()
            visited[i][j] = True
            #시작지점에서 쏘기 때문에 편의상 6으로 시작
            ts.append((i,j,6))
            #온풍기 바람이 오른쪽인 경우
            if dr == 0:
                while(len(ts)>0):
                    nowi, nowj, nowt = ts.popleft()
                    if nowt == 1:
                        continue
                    
                    #직진성 바람에 해당
                    if 0 <= nowi+dy[dr] < R and 0 <= nowj+dx[dr] < C and 1 not in wall[nowi][nowj] and visited[nowi+dy[dr]][nowj+dx[dr]] is False:
                        ts.append((nowi+dy[dr],nowj+dx[dr],nowt-1))
                        temp[nowi+dy[dr]][nowj+dx[dr]] += nowt-1
                        visited[nowi+dy[dr]][nowj+dx[dr]] = True

                    #온풍기에서 바로 쏘는 경우 직진방향만 존재하므로.
                    if nowt == 6:
                        continue
                    
                    #우측상방 대각방향 이므로 현위치에서 위쪽벽과 위에서 우측벽이 존재하지 않아야함.
                    if 0 <= nowi+dy[dr]+dy[2] < R and 0 <= nowj+dx[dr]+dx[2] < C and 0 not in wall[nowi][nowj] and 1 not in wall[nowi-1][nowj] and visited[nowi+dy[dr]+dy[2]][nowj+dx[dr]+dx[2]] is False:
                        ts.append((nowi+dy[dr]+dy[2],nowj+dx[dr]+dx[2],nowt-1))
                        temp[nowi+dy[dr]+dy[2]][nowj+dx[dr]+dx[2]] += nowt-1
                        visited[nowi+dy[dr]+dy[2]][nowj+dx[dr]+dx[2]] = True

                    #우측하방 대각방향 이므로 현위치에서 아래쪽벽과 아래에서 우측벽이 존재하지 않아야함.
                    if 0 <= nowi+dy[dr]+dy[3] < R and 0 <= nowj+dx[dr]+dx[3] < C and 0 not in wall[nowi+1][nowj] and 1 not in wall[nowi+1][nowj] and visited[nowi+dy[dr]+dy[3]][nowj+dx[dr]+dx[3]] is False:
                        ts.append((nowi+dy[dr]+dy[3],nowj+dx[dr]+dx[3],nowt-1))
                        temp[nowi+dy[dr]+dy[3]][nowj+dx[dr]+dx[3]] += nowt-1
                        visited[nowi+dy[dr]+dy[3]][nowj+dx[dr]+dx[3]] = True
            #온풍기 바람이 왼쪽인 경우
            if dr == 1:
                while(len(ts)>0):
                    nowi, nowj, nowt = ts.popleft()
                    if nowt == 1:
                        continue

                    if 0 <= nowi+dy[dr] < R and 0 <= nowj+dx[dr] < C and 1 not in wall[nowi][nowj-1] and visited[nowi+dy[dr]][nowj+dx[dr]] is False:
                        ts.append((nowi+dy[dr],nowj+dx[dr],nowt-1))
                        temp[nowi+dy[dr]][nowj+dx[dr]] += nowt-1
                        visited[nowi+dy[dr]][nowj+dx[dr]] = True

                    if nowt == 6:
                        continue

                    if 0 <= nowi+dy[dr]+dy[2] < R and 0 <= nowj+dx[dr]+dx[2] < C and 0 not in wall[nowi][nowj] and 0 not in wall[nowi-1][nowj-1] and visited[nowi+dy[dr]+dy[2]][nowj+dx[dr]+dx[2]] is False:
                        ts.append((nowi+dy[dr]+dy[2],nowj+dx[dr]+dx[2],nowt-1))
                        temp[nowi+dy[dr]+dy[2]][nowj+dx[dr]+dx[2]] += nowt-1
                        visited[nowi+dy[dr]+dy[2]][nowj+dx[dr]+dx[2]] = True

                    if 0 <= nowi+dy[dr]+dy[3] < R and 0 <= nowj+dx[dr]+dx[3] < C and 0 not in wall[nowi+1][nowj] and 0 not in wall[nowi+1][nowj-1] and visited[nowi+dy[dr]+dy[3]][nowj+dx[dr]+dx[3]] is False:
                        ts.append((nowi+dy[dr]+dy[3],nowj+dx[dr]+dx[3],nowt-1))
                        temp[nowi+dy[dr]+dy[3]][nowj+dx[dr]+dx[3]] += nowt-1
                        visited[nowi+dy[dr]+dy[3]][nowj+dx[dr]+dx[3]] = True

            #온풍기 바람이 위쪽인 경우
            if dr == 2:
                 while(len(ts)>0):
                    nowi, nowj, nowt = ts.popleft()
                    if nowt == 1:
                        continue

                    if 0 <= nowi+dy[dr] < R and 0 <= nowj+dx[dr] < C and 0 not in wall[nowi][nowj] and visited[nowi+dy[dr]][nowj+dx[dr]] is False:
                        ts.append((nowi+dy[dr],nowj+dx[dr],nowt-1))
                        temp[nowi+dy[dr]][nowj+dx[dr]] += nowt-1
                        visited[nowi+dy[dr]][nowj+dx[dr]] = True

                    if nowt == 6:
                        continue

                    if 0 <= nowi+dy[dr]+dy[0] < R and 0 <= nowj+dx[dr]+dx[0] < C and 1 not in wall[nowi][nowj] and 0 not in wall[nowi][nowj+1] and visited[nowi+dy[dr]+dy[0]][nowj+dx[dr]+dx[0]] is False:
                        ts.append((nowi+dy[dr]+dy[0],nowj+dx[dr]+dx[0],nowt-1))
                        temp[nowi+dy[dr]+dy[0]][nowj+dx[dr]+dx[0]] += nowt-1
                        visited[nowi+dy[dr]+dy[0]][nowj+dx[dr]+dx[0]] = True

                    if 0 <= nowi+dy[dr]+dy[1] < R and 0 <= nowj+dx[dr]+dx[1] < C and 1 not in wall[nowi][nowj-1] and 0 not in wall[nowi][nowj-1] and visited[nowi+dy[dr]+dy[1]][nowj+dx[dr]+dx[1]] is False:
                        ts.append((nowi+dy[dr]+dy[1],nowj+dx[dr]+dx[1],nowt-1))
                        temp[nowi+dy[dr]+dy[1]][nowj+dx[dr]+dx[1]] += nowt-1
                        visited[nowi+dy[dr]+dy[1]][nowj+dx[dr]+dx[1]] = True

            #온풍기 바람이 아래쪽인 경우
            if dr == 3:
                while(len(ts)>0):
                    nowi, nowj, nowt = ts.popleft()
                    if nowt == 1:
                        continue

                    if 0 <= nowi+dy[dr] < R and 0 <= nowj+dx[dr] < C and 0 not in wall[nowi+1][nowj] and visited[nowi+dy[dr]][nowj+dx[dr]] is False:
                        ts.append((nowi+dy[dr],nowj+dx[dr],nowt-1))
                        temp[nowi+dy[dr]][nowj+dx[dr]] += nowt-1
                        visited[nowi+dy[dr]][nowj+dx[dr]] = True

                    if nowt == 6:
                        continue

                    if 0 <= nowi+dy[dr]+dy[0] < R and 0 <= nowj+dx[dr]+dx[0] < C and 1 not in wall[nowi][nowj] and 0 not in wall[nowi+1][nowj+1] and visited[nowi+dy[dr]+dy[0]][nowj+dx[dr]+dx[0]] is False:
                        ts.append((nowi+dy[dr]+dy[0],nowj+dx[dr]+dx[0],nowt-1))
                        temp[nowi+dy[dr]+dy[0]][nowj+dx[dr]+dx[0]] += nowt-1
                        visited[nowi+dy[dr]+dy[0]][nowj+dx[dr]+dx[0]] = True

                    if 0 <= nowi+dy[dr]+dy[1] < R and 0 <= nowj+dx[dr]+dx[1] < C and 1 not in wall[nowi][nowj-1] and 0 not in wall[nowi+1][nowj-1] and visited[nowi+dy[dr]+dy[1]][nowj+dx[dr]+dx[1]] is False:
                        ts.append((nowi+dy[dr]+dy[1],nowj+dx[dr]+dx[1],nowt-1))
                        temp[nowi+dy[dr]+dy[1]][nowj+dx[dr]+dx[1]] += nowt-1
                        visited[nowi+dy[dr]+dy[1]][nowj+dx[dr]+dx[1]] = True

        if chocolate == 0: print(*temp, sep='\n')

        # 온도조절을 위해 우 좌 상 하 순으로 업데이트하기 위한 리스트    
        update = [[[0,0,0,0] for _ in range(C)] for _ in range(R)]

        #현 온도 상태를 기준으로 막혀있지 않은 부분에 대해 온도차이로 업데이트리스트를 업데이트함
        for r in range(R):
            for c in range(C):
                for di in range(4):
                    if 0 <= r+dy[di] < R and 0 <= c+dx[di] < C and temp[r][c] > temp[r+dy[di]][c+dx[di]]:
                        if di ==0 and 1 not in wall[r][c]:
                            update[r][c][di] = (temp[r][c]-temp[r+dy[di]][c+dx[di]])//4
                        if di ==1 and 1 not in wall[r][c-1]:
                            update[r][c][di] = (temp[r][c]-temp[r+dy[di]][c+dx[di]])//4
                        if di ==2 and 0 not in wall[r][c]:
                            update[r][c][di] = (temp[r][c]-temp[r+dy[di]][c+dx[di]])//4
                        if di ==3 and 0 not in wall[r+1][c]:
                            update[r][c][di] = (temp[r][c]-temp[r+dy[di]][c+dx[di]])//4

        # 위에서 구한 업데이트 내용으로 온도조절
        for r in range(R):
            for c in range(C):
                for di in range(4):
                    if update[r][c][di] != 0:
                        temp[r+dy[di]][c+dx[di]] += update[r][c][di]
                        temp[r][c] -= update[r][c][di]

        # 테두리 부분인 경우 온도 1을 낮춤
        for r in range(R):
            for c in range(C):
                if r==0 or r==R-1 or c==0 or c==C-1:
                    if temp[r][c] > 0:
                        temp[r][c] -= 1


        rr = True

        # K보다 작은 경우는 조건에 만족하지 않으므로 False 반환
        for i,j in lst_ins:
            if temp[i][j] < K:
                rr= False
                break

        return temp, rr



    R, C, K = map(int, input().split())


    table = [list(map(int,input().split())) for _ in range(R)]

    num_wall = int(input())
    tmpwall = [list(map(int,input().split())) for _ in range(num_wall)]

    wall = [[[] for _ in range(C)] for _ in range(R)]
    for y,x,t in tmpwall:
        #벽의 인덱스를 맞춰주기위해 -1
        wall[y-1][x-1].append(t)


    temp = [[0 for _ in range(C)] for _ in range(R)]

    lst_ins = []
    lst_heater = []

    #조사할 곳과 온풍기만 리스트로 가져옴.
    for i in range(R):
        for j in range(C):
            if table[i][j] == 5:
                lst_ins.append((i,j))
            elif table[i][j] != 0:
                lst_heater.append((i,j,table[i][j]-1))



    chocolate = 0

    while(True):
        #온풍기 프로세스 한 사이클을 계속 반복함.
        temp, sts = process(temp, lst_heater, wall, lst_ins, R, C, K )
    
        chocolate += 1
        if sts:
            break
        if chocolate >= 100:
            chocolate = 101
            break

    print(chocolate)
    


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