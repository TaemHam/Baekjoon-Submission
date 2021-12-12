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
from math import log, log2, ceil, floor, gcd, sqrt
#from heapq import heappush, heappop
#import bisect
#from bisect import bisect_left as bl, bisect_right as br
DEBUG = False


def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    global white
    global blue
    input = sys.stdin.readline
    n = int(input())
    mat = [list(map(int,''.join(input().split()))) for _ in range(n)]
    white = blue = 0


    def check(x, y, m):
        global white
        global blue
        total = 0

        for i in range(x,x+m):          #흰색과 파란색을 구분함
            for j in range(y,y+m):
                if mat[i][j] == 1:
                    total += 1

        if total == 0:                  #모두 흰색 혹은 파란색이면 카운트
            white += 1
        elif total == m*m:
            blue += 1

        else:                           #섞여있다면 4등분해서 다시 확인
            check(x, y, m//2)
            check(x, y + m//2, m//2)
            check(x + m//2, y, m//2)
            check(x + m//2, y + m//2, m//2)


    check(0, 0, n)
    print(white)
    print(blue)
        


    ####global ans
    ####n = int(input())
    ####logn = int(log2(n))
    ####mat = [list(map(int,''.join(list(sys.stdin.readline().split())))) for _ in range(n)]
    ####l0 = [[0] * (2**(i)) for i in range(0,logn+1)]
    ####l1 = [[1] * (2**(i)) for i in range(0,logn+1)]
    ####ans = [0,0]

    ####def cut(m):
        ####all0 = all1 = True
        ####logm = (int(log2(len(m))))
        ####for i in m:                 #안섞여있는지 확인
            ####if i != l0[logm]:
                ####all0 = False
            ####if i != l1[logm]:
                ####all1 = False
        ####if all0 or all1:           #안섞여있다면:
            ####if all0:
                ####ans[0] += 1
            ####else:
                ####ans[1] += 1
        ####else:                       #섞여있다면:
            ####halfm = len(m)//2
            ####for i in range(4):
                ####nm = []
                ####if i in [0,2]:
                    ####l,r = 0,halfm
                ####else:
                    ####l,r = halfm,len(m)
                ####for j in range(halfm):
                    ####nm = nm + [m[j+(halfm * (i//2))][l:r]]
                ####cut(nm)

    ####cut(mat)
    ####print(*ans,sep='\n')
            


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