# CP template Version 1.006
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
#from itertools import permutations
#import collections
#from collections import deque
#from collections import Counter, defaultdict as dd
#import math
#from math import log, log2, ceil, floor, gcd, sqrt
#from heapq import heappush, heappop
#import bisect
#from bisect import bisect_left as bl, bisect_right as br
DEBUG = False

def main1(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    sys.setrecursionlimit(10**6)
    ans = []
    def find(x):
        if x == parent[x]:
            return x
        else:
            r = find(parent[x])
            dist[x] += dist[parent[x]]
            parent[x] = r
            return parent[x]
    def union(x, y, k):
        xroot = parent[x]
        yroot = parent[y]
        if xroot != yroot:
            parent[yroot] = xroot
            dist[yroot] = (dist[x] + k) - dist[y]
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        parent = [i for i in range(n + 1)]
        dist = [0 for i in range(n + 1)]
        for i in range(m):
            a = list(map(str, input().split()))
            find(int(a[1]))
            find(int(a[2]))
            if a[0] == "!":
                union(int(a[1]), int(a[2]), int(a[3]))
            else:
                if parent[int(a[1])] == parent[int(a[2])]:
                    ans.append(str(dist[int(a[2])] - dist[int(a[1])]))
                else:
                    ans.append("UNKNOWN")
    
    return '\n'.join(ans)

def main2(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    def find(x):
        if x == par[x]:
            return x
        else:
            r = find(par[x])
            dif[x] += dif[par[x]]
            par[x] = r
            return par[x]

    ans = []
    while True:
        N, M = map(int, input().split())
        if N == 0 and M == 0:
            break
        par = list(range(N+1))
        dif = [0] * (N+1)

        for _ in range(M):
            qry = input().split()
            if qry[0] == '!':
                a, b, c = map(int, qry[1:])
                ar = find(a)
                br = find(b)
                if ar != br:
                    par[br] = ar
                    dif[br] = dif[a] - dif[b] + c
            elif qry[0] == '?':
                a, b = map(int, qry[1:])
                if find(a) == find(b):
                    ans.append(str(dif[b] - dif[a]))
                else:
                    ans.append('UNKNOWN')
    
    return '\n'.join(ans)

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
    a = main1() 
    b = main2()
    # print(a)
    # print(b)
    print(a == b)
    