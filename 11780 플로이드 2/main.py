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
    m = int(input().strip())
    inf = 987654321
    grp = [[inf for _ in range(n)] for _ in range(n)]

    route = [[-1 for _ in range(n)] for _ in range(n)]

    def find_path(s,e):
        if route[s][e] == -1:
            return []
        m = route[s][e]
        return find_path(s,m) + [m+1] + find_path(m,e)

    for _ in range(m):
        s, e, c = map(int,input().split())
        grp[s-1][e-1] = min(grp[s-1][e-1], c)
    
    for mid in range(n):
        for stt in range(n):
            for end in range(n):
                if stt != end and grp[stt][end] > grp[stt][mid] + grp[mid][end]:
                    grp[stt][end] = grp[stt][mid] + grp[mid][end]
                    route[stt][end] = mid
    
    for i in range(n):
        for j in range(n):
            if grp[i][j] == inf:
                grp[i][j] = 0
        print(*grp[i], sep=' ')
    
    for i in range(n):
        for j in range(n):
            if grp[i][j] == 0:
                print(0)
            else:
                path = [i+1] + find_path(i,j) + [j+1]
                print(len(path), *path, sep = ' ')
    

    


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