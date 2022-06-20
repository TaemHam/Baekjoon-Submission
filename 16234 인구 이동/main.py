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

    # 방문 배열을 시간으로 저장하면, 계속해서 0으로 초기화 하지 않아도 방문 배열 재사용 가능

    N, L, R = map(int, input().split())
    K = N+1
    mov = (1, -1, K, -K)
    ans = 2000
    brd = [-1] * N*K
    vis = [-1] * N*K + [2000] * K
    cque = [xy for y in range(0, N*K, K) for xy in range(y, y+N)]

    for y in range(0, N*K, K):
        vis[y+N] = 2000
        brd[y:y+N] = map(int, input().split())
    
    for time in range(2000): # 2000일째를 돌리지 않아도 1999일째가 끝나면 정답이 2000으로 나오게 됨 

        nque = []
        for xy in cque:
            if vis[xy] == time:
                continue
            vis[xy] = time
            ttl = brd[xy]
            que = [xy]

            for crd in que:
                for d in mov:
                    if vis[crd+d] < time and L <= abs(brd[crd] - brd[crd+d]) <= R:
                        vis[crd+d] = time
                        ttl += brd[crd+d]
                        que.append(crd+d)
            
            if len(que) > 1:
                nque.extend(que)
                ttl //= len(que)
                for crd in que:
                    brd[crd] = ttl
        
        if not nque:
            ans = time
            break

        cque = nque
    
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