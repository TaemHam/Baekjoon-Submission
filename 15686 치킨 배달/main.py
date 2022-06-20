# CP template Version 1.006
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
#from itertools import combinations
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
    
    def comb_type2(arr, ret, cache, cnt, idx):
        if cnt == 1:
            ret.append(cache + [arr[idx]])
        else:
            comb_type2(arr, ret, cache + [arr[idx]], cnt - 1, idx + 1)
            if len(arr) - idx - 1 >= cnt:
                comb_type2(arr, ret, cache, cnt, idx + 1)

    N, M = map(int, input().split())
    jip, chi = [], []
    ans = int(1e9)
    for y in range(N):
        brd = input().split()
        for x in range(N):
            if brd[x] == '1':
                jip.append((y, x))
            elif brd[x] == '2':
                chi.append((y, x))
    
    grp = []
    for i in range(len(jip)):
        tmp = []
        for j in range(len(chi)):
            tmp.append(abs(jip[i][0] - chi[j][0]) + abs(jip[i][1] - chi[j][1]))
        grp.append(tmp)
    
    for arr in combinations(range(len(chi)), M):
        res = 0
        for e in grp:
            mnm = int(1e9)
            for k in arr:
                mnm = min(mnm, e[k])
            res += mnm
        ans = min(ans, res)

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