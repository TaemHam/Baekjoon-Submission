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

    N, M, K = map(int, input().split())
    L = M + 1
    ans = 101
    chk = []
    htr = []
    cnd = []
    wnd = [0] * N*L
    brd = [0] * N*L
    oob = [1] * N*L + [0] * L
    wll = [[0] * N*L for _ in range(4)]
    chg = (0, 0, 2, 1, 3)
    mov = [1, -L, -1, L]

    for y in range(0, N*L, L):
        oob[y+M] = 0
        for x, e in enumerate(map(int, input().split())):
            if not e:
                continue
            elif e == 5:
                chk.append(y+x)
            else:
                htr.append((y+x, chg[e]))

    for _ in range(int(input().strip())):
        y, x, t = map(lambda x: int(x)-1, input().split()) # 입력 거꾸로 주의! 0에는 오른쪽 벽, 1에는 윗쪽 벽
        if t:
            wll[1][y*L+x] = 1    # 0은 우측, 1은 상단, 2는 좌측, 3은 하단에 벽이 있음 
            wll[3][y*L+x-L] = 1
        else:
            wll[0][y*L+x] = 1
            wll[2][y*L+x+1] = 1
        
    for loc, dir in htr:
        vis = [0] * N*L
        wnd[loc+mov[dir]] += 5
        cque = [loc+mov[dir]]
        nque = []

        for heat in range(4, 0, -1):
            
            for cur in cque:

                nxt = cur+mov[dir]
                
                if oob[nxt+mov[dir-3]] and not wll[dir][cur+mov[dir-3]] | wll[dir-3][cur] and not vis[nxt+mov[dir-3]]:
                    wnd[nxt+mov[dir-3]] += heat
                    vis[nxt+mov[dir-3]] = 1
                    nque.append(nxt+mov[dir-3])

                if oob[nxt] and not wll[dir][cur] and not vis[nxt]:
                    wnd[nxt] += heat
                    vis[nxt] = 1
                    nque.append(nxt)

                if oob[nxt+mov[dir-1]] and not wll[dir][cur+mov[dir-1]] | wll[dir-1][cur] and not vis[nxt+mov[dir-1]]:
                    wnd[nxt+mov[dir-1]] += heat
                    vis[nxt+mov[dir-1]] = 1
                    nque.append(nxt+mov[dir-1])

            if not nque:
                break
            cque, nque = nque, []
    
    for i in range(N*L):
        if wnd[i]:
            cnd.append(i)
 
    for choco in range(1, 101):
        
        '''온풍기 바람 페이즈'''
        for i in cnd:
            brd[i] += wnd[i]

        '''온도 조절 페이즈'''
        dif = [0] * N*L
        for y in range(0, N*L, L):
            for xy in range(y, y+M-1):
                if not wll[0][xy] and int((brd[xy] - brd[xy+1])/4):
                    dif[xy] -= int((brd[xy] - brd[xy+1])/4)
                    dif[xy+1] += int((brd[xy] - brd[xy+1])/4)
        for y in range(0, N*L-L, L):
            for xy in range(y, y+M):
                if not wll[3][xy] and int((brd[xy] - brd[xy+L])/4):
                    dif[xy] -= int((brd[xy] - brd[xy+L])/4)
                    dif[xy+L] += int((brd[xy] - brd[xy+L])/4)
        for i in range(len(dif)):
            brd[i] += dif[i]
            
        
        '''바깥 온도 페이즈'''
        for x in range(1, M-1):
            if brd[x]:
                brd[x] -= 1
            if brd[N*L-L+x]:
                brd[N*L-L+x] -= 1
        for y in range(0, N*L, L):
            if brd[y]:
                brd[y] -= 1
            if brd[M-1+y]:
                brd[M-1+y] -= 1
        
        '''온도 체크 페이즈'''
        for i in chk:
            if brd[i] < K:
                break
        else:
            ans = choco
            break
        
    print(ans)
    for y in range(0, N*L, L):
        print(wnd[y:y+M])

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