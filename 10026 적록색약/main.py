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
#from bisect import bisect_left as bl, bisect_right as br
DEBUG = False


def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    input = sys.stdin.readline
    n = int(input().strip())
    graph = []
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    v = set()
    v2 = set()
    q = []
    cnt = [0] * 3                       

    def dfs(q,c,v,cnt):
        t = q[0]
        if len(c) == 2 and t in v:
            q.pop()
            return cnt
        while q:
            x,y = q.pop()
            if (x,y) not in v:
                v.add((x,y))
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] in c:
                        q.append((nx,ny))

        if len(c) == 2:
            cnt[2] += 1
            return cnt
        elif 'B' in c:
            cnt[1] += 1
            return cnt
        else:
            cnt[0] += 1
            c = c.union(('R','G'))
            q.append(t)
            return dfs(q,c,v2,cnt)

    for i in range(n):
        t = input().strip()
        graph.append(t)
    
    for x in range(n):
        for y in range(n):
            if (x,y) not in v:
                q.append((x,y))
                c = set(graph[x][y])
                cnt = dfs(q,c,v,cnt)

    print(cnt[0]+cnt[1], cnt[1]+cnt[2])
    


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