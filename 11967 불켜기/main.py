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
#from heapq import heappush, heapreplace
#import bisect
#from bisect import bisect_left as bl, bisect_right as br
DEBUG = False


def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    N, M = map(int, input().split())
    L = N+1
    grp = [[] for _ in range(L*L)]
    for _ in range(M):
        sy, sx, ey, ex = map(lambda x: int(x)-1, input().split())
        grp[sy*L+sx].append(ey*L+ex)
    oob = [0] * L*N + [1] * N
    for y in range(0, L*N, L):
        oob[y+N] = 1
    dir = [1, -1, L, -L]
    chk = [0] * L*L
    lit = [0] * L*L
    vst = [0] * L*L
    vque = [0]
    chk[1], chk[L] = 1, 1
    vst[0], lit[0] = 1, 1
    
    for cur in vque:

        for nxt in grp[cur]:
            lit[nxt] = 1
            if chk[nxt]:
                chk[nxt] = 0
                vst[nxt] = 1
                vque.append(nxt)
                
                for d in dir:
                    if oob[nxt+d] or vst[nxt+d]:
                        continue
                    if lit[nxt+d]:
                        vst[nxt+d] = 1
                        vque.append(nxt+d)
                    else:
                        chk[nxt+d] = 1
        

    print(sum(lit))

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