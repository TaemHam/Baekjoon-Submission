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
#from bisect import bisect_left as bl, bisect_right as br
DEBUG = False

def main(f=None):
    init(f)
    #sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    ans = []
    for _ in range(int(input().strip())):
        arr = [list(map(int, input().split())) for _ in range(int(input().strip()))]
        arr = sorted(arr, key= lambda x: -x[1])
        n, m = 1, arr[0][1]
        for i in range(len(arr)):
            if arr[i][1] != m:
                m = arr[i][1]
                n += 1
            arr[i][1] = n

        arr = sorted(arr, key= lambda x: x[0])
        h = 2**(len(format(n-1, 'b')))
        grp = [0] * 2*h
        h -= 1
        res = 0
        
        for _, y in arr:
            y += h
            l, r = h+1, y
            while l <= r:
                if l&1: 
                    res += grp[l]
                    l += 1
                if not r&1:
                    res += grp[r]
                    r -= 1
                l >>= 1
                r >>= 1
            
            grp[y] += 1
            while y > 1:
                y >>= 1
                grp[y] = grp[y*2] + grp[y*2+1]
                
        ans.append(str(res))
    
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
    