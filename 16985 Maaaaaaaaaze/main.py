# CP template Version 1.006
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
from itertools import permutations
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

    def rotate(x):
        maze[x:x+3], maze[x+4:x+17:6], maze[x+28:x+25:-1], maze[x+24:x+11:-6] = maze[x+4:x+17:6], maze[x+28:x+25:-1], maze[x+24:x+11:-6], maze[x:x+3]
        maze[x+6:x+9], maze[x+3:x+16:6], maze[x+22:x+19:-1], maze[x+25:x+12:-6] = maze[x+3:x+16:6], maze[x+22:x+19:-1], maze[x+25:x+12:-6], maze[x+6:x+9]

    mov = (1, -1, 6, -6, 36, -36)
    tgt = 172
    ans = 216
    brd = [['0'] * 36 for _ in range(5)]
    vis = [-1] * 180 + [122880] * 36
    vis[0] = 122880
    v = -1
    for i in range(5):
        vis[i*36+30:i*36+36] = [122880] * 6
        for y in range(0, 30, 6):
            vis[i*36+y+5] = 122880
            brd[i][y:y+5] = input().split()
    
    for a, b, c, d, e in permutations(range(5), 5):
        maze = brd[a] + brd[b] + brd[c] + brd[d] + brd[e]
        for i in range(1, 1024):
            if maze[0] == '1' and maze[tgt] == '1':
                cque = [0]
                v += 1
                for time in range(216):
                    nque = []
                    for cur in cque:
                        if cur == tgt:
                            if time == 12:
                                return 12
                            ans = min(ans, time)
                            nque = []
                            break
                        for dir in mov:
                            if vis[cur+dir] < v and maze[cur+dir] == '1':
                                vis[cur+dir] = v
                                nque.append(cur+dir)
                    if not nque:
                        break
                    cque = nque
            
            rotate(0)
            for j in range(36, 180, 36):
                if not i%4:
                    i //= 4
                    rotate(j)
                else:
                    break
        
    return(ans if ans != 216 else -1)

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
    print(main())