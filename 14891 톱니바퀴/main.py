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

    ans = 0
    cog = [int(input().strip(), 2) for _ in range(4)]

    for _ in range(int(input().strip())):
        num, dir = map(int, input().split())
        rtt = [0] * 4
        rtt[num-1] = dir
        for i in range(num-2, -1, -1):
            if (cog[i] & 1<<5)>>4 ^ (cog[i+1] & 1<<1):
                rtt[i] = -rtt[i+1]
            else:
                break
        for i in range(num-1, 3, 1):
            if (cog[i] & 1<<5)>>4 ^ (cog[i+1] & 1<<1):
                rtt[i+1] = -rtt[i]
            else:
                break
        
        for i in range(4):
            if rtt[i] == -1:
                cog[i] <<= 1
                if cog[i] & 1<<8:
                    cog[i] |= 1
                cog[i] &= (1<<8) - 1
            elif rtt[i] == 1:
                if cog[i] & 1:
                    cog[i] |= 1<<8
                cog[i] >>= 1
        
    for i in range(4):
        if cog[i] & 1<<7:
            ans |= 1<<i
    
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