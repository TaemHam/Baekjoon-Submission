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
#from bisect import bisect_left as bl
DEBUG = False


def main(f=None):
    init(f)
    # ######## INPUT AREA BEGIN ##########

    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]
    N, K = map(int, input().split())
    flp = [1, 0, 3, 2]
    tbl = [input().split() for _ in range(N)]
    loc = []
    dir = []
    brd = [[[] for _ in range(N)] for _ in range(N)]
    stk = []
    ans = -1

    for i in range(K):
        y, x, d = map(lambda x: int(x)-1, input().split())
        loc.append((y, x))
        dir.append(d)
        brd[y][x].append(i)
    
    for t in range(1, 1001):
        for cur in range(K):
            y, x = loc[cur]
            ny = y + dy[dir[cur]]
            nx = x + dx[dir[cur]]
            if 0 > ny or N <= ny or 0 > nx or N <= nx or tbl[ny][nx] == '2':
                dir[cur] = flp[dir[cur]]
                ny = y + dy[dir[cur]]
                nx = x + dx[dir[cur]]
                if 0 > ny or N <= ny or 0 > nx or N <= nx or tbl[ny][nx] == '2':
                    continue

            while True:
                mov = brd[y][x].pop()
                loc[mov] = (ny, nx)
                if tbl[ny][nx] == '1':
                    brd[ny][nx].append(mov)
                else:
                    stk.append(mov)
                if mov == cur:
                    while stk:
                        brd[ny][nx].append(stk.pop())
                    break

            if len(brd[ny][nx]) >= 4:
                ans = t
                break
        
        if ans != -1:
            break
    
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
    main()