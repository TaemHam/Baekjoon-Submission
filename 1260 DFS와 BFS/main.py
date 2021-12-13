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
from heapq import heappush, heappop
#import bisect
#from bisect import bisect_left as bl, bisect_right as br
DEBUG = False


def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    input = sys.stdin.readline
    n, m, v = map(int, input().split())
    g_b = [[] for _ in range(n+1)]
    q = deque([v])

    for _ in range(m):
        i, j = map(int, input().split())
        heappush(g_b[i],j)
        heappush(g_b[j],i)

    g_d = []
    for i in g_b:
        g_d.append(i[::-1])

    def dfs(q,g):
        l = []
        while q:
            t = q.pop()
            if t not in l:
                l.append(t)
                for i in g[t]:
                    if i not in l:
                        q.append(i)
        return l
    
    def bfs(q,g):
        l = []
        while q:
            t = q.popleft()
            if t not in l:
                l.append(t)
                for i in g[t]:
                    if i not in l:
                        q.append(i)
        return l

    q = deque([v])
    print(*dfs(q,g_d))
    q = deque([v])
    print(*bfs(q,g_b))

    ####input = sys.stdin.readline
    ####n, m, v = map(int, input().split())
    ####g = [[0 for _ in range(n+1)] for _ in range(n+1)]

    ####for _ in range(m):
        ####i, j = map(int, input().split())
        ####g[i][j] = 1
        ####g[j][i] = 1

    ####def dfs(v,l):
        ####l += [v]
        ####for i in range(n+1):
            ####if g[v][i] == 1 and i not in l:
                ####dfs(i,l)
        ####return l

    ####def bfs(v):
        ####l = [v]
        ####q = deque([v])
        ####while q:
            ####t = q.popleft()
            ####for i in range(n+1):
                ####if g[t][i] == 1 and i not in l:
                    ####l.append(i)
                    ####q.append(i)
        ####return l

    ####print(dfs(v,[]))
    ####print(bfs(v))
    

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