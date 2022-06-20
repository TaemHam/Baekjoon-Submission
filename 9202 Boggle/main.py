# CP template Version 1.006
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
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########
    
    def insert(wrd, dic):
        for alp in map(lambda x: ord(x) - 64, wrd):
            if not dic[alp]:
                dic[alp] = [0] * 27
            dic = dic[alp]
        dic[0] = 1

    dic = [0] * 27
    for _ in range(int(input().strip())):
        insert(input().strip(), dic)
    input()

    ans = []
    mov = (-6, -5, -4, -1, 1, 4, 5, 6)
    scr = (0, 0, 0, 1, 1, 2, 3, 5, 11)

    for _ in range(int(input().strip())):
        res = set()
        brd = [0] * 25
        for y in range(0, 20, 5):
            brd[y:y+4] = map(lambda x: ord(x) - 64, input().strip())
        
        input()
        for y in range(0, 20, 5):
            for xy in range(y, y+4):
                if dic[brd[xy]]:
                    que = [(xy, dic[brd[xy]], 1<<xy, chr(brd[xy]+64))]
                    for cur, fnd, vis, wrd in que:
                        if fnd[0]:
                            res.add(wrd)
                        for dir in mov:
                            if brd[cur+dir] and not vis & 1<<cur+dir and fnd[brd[cur+dir]]:
                                que.append((cur+dir, fnd[brd[cur+dir]], vis | 1<<cur+dir, wrd+chr(brd[cur+dir]+64)))
        res.discard('')

        ans.append(f'{sum(scr[len(x)] for x in res)} {min(res, key= lambda x: (-len(x), x))} {len(res)}')
    
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