# CP template Version 1.006
#import io
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
#from itertools import combinations
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
    mov = (1, L, -1, -L)
    vis = [0] * N*L
    brd = ''
    ans = '-1'
    for _ in range(N):
        brd += input().strip() + '#'
    brd += '#' * L
    stt = brd.index('S')
    dst = brd.index('C')
    vis[stt] = 15
    cque = [(stt, -1, 0, -1)]


    for time in range(0, N*L*10):
        nque = []
        for cur, pd, flg, flg2 in cque:
            if brd[cur] == 'C' and cur != flg2:
                if flg:
                    ans = str(time)
                    nque = []
                    break
                flg = 4 if cur == dst else 8
                flg2 = cur

            for d in range(4):
                if d == pd or brd[cur+mov[d]] == '#' or vis[cur+mov[d]] & 1<<d+flg:
                    continue
                vis[cur+mov[d]] |= 1<<d+flg
                nque.append((cur+mov[d], d, flg, flg2))
        
        if not nque:
            break
        cque = nque
    
    return ans
    


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