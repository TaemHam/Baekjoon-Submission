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

    N, M = map(int, input().split())
    L = M+1
    mov = (1, -1, L, -L)
    brd = [0] * (N+1)*L
    dic = {}
    prv = 0
    ans = 0
    cque = set()
    for y in range(0, N*L, L):
        brd[y:y+M] = map(int, list(input().strip()))
        for xy in range(y, y+M):
            if brd[xy] in dic:
                dic[brd[xy]].add(xy)
            else:
                dic[brd[xy]] = {xy}
    
    for lvl in sorted(dic.keys())[:-1]:

        ans += len(cque) * (lvl-prv)
        for cur in cque:
            brd[cur] = lvl

        cque |= dic[lvl]
        nque = set()
        vis = [0] * N*L

        for cur in cque:
            if not vis[cur]:
                for d in mov:
                    if brd[cur+d] < lvl:
                        pque = [cur]
                        vis[cur] = 1
                        for pcur in pque:
                            nque.discard(pcur)
                            for pd in mov:
                                if brd[pcur+pd] == lvl and not vis[pcur+pd]:
                                    vis[pcur+pd] = 1
                                    pque.append(pcur+pd)
                        break
                else:
                    nque.add(cur)
        
        cque = nque
        prv = lvl
        
    print(ans + len(cque) * (max(dic.keys())-prv))
            
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