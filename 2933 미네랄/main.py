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
    L = M+1
    mov = (L, -L, 1, -1)
    brd = ['x'] * L*(N+1)
    for y in range(0, N*L, L):
        brd[y:y+M] = list(input().strip())
    K = int(input().strip())
    arr = list(map(lambda x: N - int(x), input().split()))
    vis = [-1] * L*N + [K] * L
    vis[M:L*N:L] = [K] * N
    for k in range(K):
        l, r, d = (M-1, -1, -1) if k%2 else (0, M, 1)
        for xy in range(l + arr[k]*L, r + arr[k]*L, d):
            if brd[xy] == 'x':
                brd[xy] = '.'
                for i in range(4):
                    cxy = xy + mov[i]
                    if vis[cxy] < k and brd[cxy] == 'x':
                        que = [(cxy)]
                        vis[cxy] = k
                        bot = [-1] * M
                        for nxy in que:
                            if nxy > bot[nxy%L]:
                                bot[nxy%L] = nxy
                            for d in mov:
                                if vis[nxy+d] < k and brd[nxy+d] == 'x':
                                    vis[nxy+d] = k
                                    que.append(nxy+d)

                        if max(bot)//L == N-1:
                            continue

                        mdf = int(1e9)
                        for txy in bot:
                            if txy == -1:
                                continue
                            for kxy in range(txy, L*N, L):
                                if brd[kxy+L] == 'x':
                                    break
                            mdf = min(mdf, kxy-txy)

                        for nxy in sorted(que, reverse= True):
                            brd[nxy], brd[nxy+mdf] = brd[nxy+mdf], brd[nxy]
                        break
                break

    ans = []
    for y in range(0, N*L, L):
        ans.append(''.join(brd[y:y+M]))
        
    return '\n'.join(ans)

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
    print(main())