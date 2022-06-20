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

    def block(arr, lt, rt, rb, lb):
        arr[0] += lt + rt + rb + lb
        arr[1] -= lt
        arr[2] -= rt
        arr[3] -= rb
        arr[4] -= lb

    N = int(input().strip())
    DL, DR = N-1, N+1
    brd = []
    for _ in range(N):
        brd.extend(map(int, input().split()))
    ori = [brd[1] + brd[N] + brd[N+1] + brd[N+2] + brd[N+N+1], brd[0], sum(brd[2:N]+brd[3+N:2*N]), sum(brd[N+N:N*N:N]), sum(brd[N+N:])]
    ori[4] -= ori[3] + brd[N+N+1]
    top, rgt, bot, lft = 1, N+2, N+N+1, N
    ans = 400000

    for d1 in range(1, N-1):
        nxt = ori[:]

        for d2 in range(1, N-d1):
            que = [nxt[:]] * (N-d1-d2)

            for i in range(len(que)-1):
                que[i] = que[i][:]
                add3 = sum(brd[i+bot+N:N*N:N])
                block(que[i+1], 
                    -sum(brd[i+top:i+lft:DL]), 
                    sum(brd[i+rgt+1:i+top:-DR]), 
                    -sum(brd[i+lft:i+bot+1:DR])-add3, 
                    sum(brd[i+bot+1:i+rgt+1:-DL])+add3)

            for x in range(len(que)):
                cpy = que[x]
                ans = min(ans, max(cpy)-min(cpy))

                for xy in range(x, N*len(que)-N, N):
                    add1 = sum(brd[(d1+xy//N)*N:xy+lft])
                    add2 = sum(brd[xy+rgt+DR:((xy+rgt)//N+2)*N])
                    block(cpy,
                        -sum(brd[xy+top:xy+lft+1:DL])-add1, 
                        -sum(brd[xy+rgt:xy+top:-DR])-add2, 
                        sum(brd[xy+lft+N:xy+bot+N:DR])+add1, 
                        sum(brd[xy+bot+N:xy+rgt-1+N:-DL])+add2)
                    ans = min(ans, max(cpy)-min(cpy))
                    
            if d2 < N-d1-1:
                add3 = sum(brd[bot+N:N*N:N])
                rgt += DR
                bot += DR
                add2 = sum(brd[rgt+1:rgt+N-d1-d2-1])
                add5 = sum(brd[rgt-1:bot-1:DL]) + sum(brd[rgt:bot+1:DL])
                block(nxt, 0, -add2, -add3, add2+add3+add5)

        top += 1
        lft += N
        bot = lft+DR
        rgt = top+DR
        block(ori, -sum(brd[top-1:lft-DL:DL]), brd[top]+brd[rgt], brd[lft], sum(brd[bot:rgt:-DL]))
    
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