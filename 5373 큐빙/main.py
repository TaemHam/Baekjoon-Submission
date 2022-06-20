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

    ans = []
    dic = { 
        'U': (0, (3, 2, -1), (5, 2, -1), (2, 2, -1), (4, 2, -1)), 
        'D': (1, (3, 6, 1), (4, 6, 1), (2, 6, 1), (5, 6, 1)), 
        'F': (2, (0, 6, 1), (5, 0, 3), (1, 6, 1), (4, 8, -3)), 
        'B': (3, (0, 2, -1), (4, 0, 3), (1, 2, -1), (5, 8, -3)), 
        'L': (4, (0, 0, 3), (2, 0, 3), (1, 8, -3), (3, 8, -3)),
        'R': (5, (0, 8, -3), (3, 0, 3), (1, 0, 3), (2, 8, -3)),
        '+': 1,
        '-': 0}

    for _ in range(int(input().strip())):

        cube = [['w']*9, ['y']*9, ['r']*9, ['o']*9, ['g']*9, ['b']*9]
        input()

        for cmd in input().split():
            (frt, (top, tl, tr), (rgt, rl, rr), (bot, bl, br), (lft, ll, lr)), dir = map(lambda x: dic[x], list(cmd))
            
            if dir:
                cube[frt] = cube[frt][6::-3] + cube[frt][7::-3] + cube[frt][8::-3]
                cube[top][tl::tr], cube[rgt][rl::rr], cube[bot][bl::br], cube[lft][ll::lr] = cube[lft][ll::lr], cube[top][tl::tr], cube[rgt][rl::rr], cube[bot][bl::br]
            else:
                cube[frt] = cube[frt][2::3] + cube[frt][1::3] + cube[frt][0::3]
                cube[top][tl::tr], cube[rgt][rl::rr], cube[bot][bl::br], cube[lft][ll::lr] = cube[rgt][rl::rr], cube[bot][bl::br], cube[lft][ll::lr], cube[top][tl::tr]

        for i in range(0, 9, 3):
            ans.append(''.join(cube[0][i:i+3]))
    
    print('\n'.join(ans))

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