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

    def isrt(tri, wrd):
        cur = 0
        for alp in wrd:
            num = ord(alp) - 96
            if tri[cur][num] == -1:
                tri[cur][num] = len(tri)
                tri.append(ori[:])
            cur = tri[cur][num]
        tri[cur][0] = 1

    C, N = map(int, input().split())
    ori = [0] + [-1] * 26
    clr = [ori[:]]
    nik = set()
    ans = []
    for _ in range(C):
        isrt(clr, input().strip())
    for _ in range(N):
        nik.add(input().strip())
    
    for _ in range(int(input().strip())):
        team = input().strip()
        ccur = 0
        for i in range(len(team)):
            if clr[ccur][0]:
                if team[i:] in nik:
                    ans.append('Yes')
                    break
            ccur = clr[ccur][ord(team[i])-96]
            if ccur == -1:
                ans.append('No')
                break
        else:
            ans.append('No')
    
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
    print(main())