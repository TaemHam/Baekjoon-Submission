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

    calc = lambda a, b, c: a + c if b == '+' else a * c if b == '*' else a - c

    input()
    pque = set() # 이전큐
    cque = set() # 현재큐
    nque = set() # 다음큐

    arr = list(input().strip())
    num = list(map(int, arr[::2]))
    opr = [0] + arr[1::2]

    cque.add(num[0])

    for i in range(1, len(num)):

        # 괄호 없을 때, 현재 숫자(num[i])와 현재큐 값들(cque)과 연산 한 결과를 다음큐(nque)에 저장
        for x in cque:
            nque.add(calc(x, opr[i], num[i]))
        
        # 괄호 있을 때, 현재 숫자와 이전 숫자를 연산한 값에 이전큐 값들(pque)과 연산한 결과를 다음큐에 저장
        for x in pque:
            nque.add(calc(x, opr[i-1], calc(num[i-1], opr[i], num[i])))

        # 이전큐는 현재큐로, 현재큐는 다음큐로, 다음큐는 빈 셋으로 스왑
        pque, cque, nque = cque, nque, set()

    print(max(cque))

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