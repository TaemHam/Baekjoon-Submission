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

    ans = []
    while True:
        N, M = map(int, input().split())
        if N == 0:
            break
        L = N+1
        res = -1
        dir = [1, -1, L, -L]
        dic = dict()
        brd = ''
        for y in range(0, L*M, L):
            brd += input().strip() + 'x'
            for xy in range(y, y+N):
                if brd[xy] == '.' or brd[xy] == 'x':
                    continue
                elif brd[xy] == '*':
                    dic[xy] = len(dic)
                else:
                    stt = xy 
        brd += 'x' * N
        log = [[0] * L*M for _ in range(2**len(dic))]
        log[0][stt] = 1
        end = -1 + 2**len(dic)
        
        cque = [(stt, 0)]
        for step in range(4000):
            nque = []
            for cur, vis in cque:
                if vis == end:
                    res = step
                    nque.clear()
                    break
                for d in dir:
                    if brd[cur+d] == 'x' or log[vis][cur+d]:
                        continue
                    log[vis][cur+d] = 1
                    if brd[cur+d] == '*':
                        nvis = vis | 1<<dic[cur+d]
                        log[nvis][cur+d] = 1
                        nque.append((cur+d, nvis))
                    else:
                        nque.append((cur+d, vis))
            
            if not nque:
                break
            cque = nque
        
        ans.append(str(res))
    
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