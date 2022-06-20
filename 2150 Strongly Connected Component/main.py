# CP template Version 1.006
#import io
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
#from bisect import bisect_left as bl, bisect_roloc[xyight as brloc[xy]
DEBUG = False

def main(f=None):
    init(f)
    sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    def dfs1(cur):
        vis[cur] = 1
        for nxt in fwd[cur]:
            if not vis[nxt]:
                dfs1(nxt)
        stk.append(cur)
    
    def dfs2(cur):
        vis[cur] = 0
        for nxt in bwd[cur]:
            if vis[nxt]:
                tmp.append(nxt)
                dfs2(nxt)

    V, E = map(int, input().split())
    fwd = [[] for _ in range(V+1)]
    bwd = [[] for _ in range(V+1)]
    vis = [0] * (V+1)
    stk = []
    ans = []
    res = []
    for _ in range(E):
        a, b = map(int, input().split())
        fwd[a].append(b)
        bwd[b].append(a)
    
    for i in range(1, V+1):
        if not vis[i]:
            dfs1(i)
    
    for i in stk[::-1]:
        if vis[i]:
            tmp = [i]
            dfs2(i)
            res.append(sorted(tmp))

    ans.append(str(len(res)))
    for arr in sorted(res, key = lambda x: x[0]):
        ans.append(' '.join(map(str, arr)) + ' -1')
    
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
    