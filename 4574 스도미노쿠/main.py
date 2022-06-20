# CP template Version 1.006
# import io
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
#from itertools import combinations
#import collections
#from collections import deque
#from collections import Counter, defaultdict as dd
#import math
#from math import log, log2, ceil, floor, gcd, sqrt
#from heapq import heappush, heappop
#import bisect
#from bisect import insort_left as il
DEBUG = False


def main(f=None):
    init(f)
    # ######## INPUT AREA BEGIN ##########

    idxfy = lambda x: ord(x[0])*10+int(x[1])-651

    def numpop(x):
        std = x//30*30 + x%10//3*3
        nums = [0] * 10
        for i in brd[x//10*10:x//10*10+9]:
            nums[i] = 1
        for i in brd[x%10:90:10]:
            nums[i] = 1
        for i in brd[std:std+3]+brd[std+10:std+13]+brd[std+20:std+23]:
            nums[i] = 1
        res = []
        for i in range(1, 10):
            if not nums[i]:
                res.append(i)

        return res
    
    def dfs(usd):

        for cur in range(90):
            if not brd[cur]:
                break
        else:
            return 1

        anum = numpop(cur)
        if not brd[cur+1]:
            bnum = numpop(cur+1)
            for a in anum:
                for b in bnum:
                    if a != b:
                        i, j = (a, b) if a<b else (b, a)
                        if not usd & 1<<(bit[i] + j-i):
                            brd[cur], brd[cur+1] = a, b
                            if dfs(usd|1<<(bit[i] + j-i)):
                                return 1
                            brd[cur], brd[cur+1] = 0, 0
                            
        if not brd[cur+10]:
            bnum = numpop(cur+10)
            for a in anum:
                for b in bnum:
                    if a != b:
                        i, j = (a, b) if a<b else (b, a)
                        if not usd & 1<<(bit[i] + j-i):
                            brd[cur], brd[cur+10] = a, b
                            if dfs(usd|1<<(bit[i] + j-i)):
                                return 1
                            brd[cur], brd[cur+10] = 0, 0
        return 0

    bit = (0, -1, 7, 14, 20, 25, 29, 32, 34)
    ori = [0] * 90 + [1] * 10
    for i in range(9, 90, 10):
        ori[i] = 1
    ans = []

    while True:
        N = int(input().strip())
        if not N: 
            break
        
        usd = 0
        brd = ori[:]

        for _ in range(N):
            a, acrd, b, bcrd = input().split()
            a, b = int(a), int(b)
            brd[idxfy(acrd)], brd[idxfy(bcrd)] = a, b
            if a > b:
                a, b = b, a
            usd |= 1<<(bit[a] + b-a)
        
        for x, xcrd in enumerate(input().split(), 1):
            brd[idxfy(xcrd)] = x

        dfs(usd)

        res = []
        for y in range(0, 90, 10):
            res.append(''.join(map(str, brd[y:y+9])))
        ans.append(f'Puzzle {len(ans)+1}'+'\n'+'\n'.join(res))
    
    return '\n'.join(ans)


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
    input = sys.stdin.readline # io.BytesIO(os.read(0, os.fstat(0).st_size)).readline 
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