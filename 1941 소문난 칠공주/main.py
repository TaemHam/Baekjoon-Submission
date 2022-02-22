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
    
    dd = [-1, 1, -5, 5]
    max_size = 1
    for i in range(24, 17, -1):
        max_size |= 1 << i
    log = [0] * max_size
    brd = [0] * 25
    ans = set()
    for y in range(0, 25, 5):
        tmp = input().strip()
        for x in range(5):
            if tmp[x] == 'S':
                brd[y+x] = 1
    
    for p in range(25):
        log[p] = 1
        q = [(1 << p, set([p]), brd[p])]
        while q:
            vis, arr, cnt = q.pop()

            if len(arr) == 7:
                if cnt >= 4:
                    ans.add(vis)
                continue
            
            for prv in arr:
                for i in range(4):
                    nxt = prv + dd[i]
                    if 0 <= nxt < 25 and abs(nxt%5 - prv%5) != 4 and not vis & (1<<nxt):
                        nvis = vis | (1<<nxt)
                        if not log[nvis]:
                            log[nvis] = 1
                            q.append((vis | (1<<nxt), arr.union([nxt]), cnt + brd[nxt]))
    
    print(len(ans))

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