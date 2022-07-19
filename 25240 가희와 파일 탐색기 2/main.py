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
#from bisect import bisect_left as bl
DEBUG = False

def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    def check(oprt, prms):
        if oprt == 'R':
            res = 6 & prms
        elif oprt == 'W':
            res = 2 & prms
        else: #oprt == 'X':
            res = 1 & prms
        ans.append('1' if res else '0')

    U, F = map(int, input().split())
    grp_dic = {}
    prm_dic = {}
    for _ in range(U):
        user_name, *user_group = input().split()
        if user_name in grp_dic:
            grp_dic[user_name].append(user_name)
        else:
            grp_dic[user_name] = [user_name]

        if user_group:
            for group_name in user_group[0].split(','):
                if group_name in grp_dic:
                    grp_dic[group_name].append(user_name)
                else:
                    grp_dic[group_name] = [user_name]
    
    for _ in range(F):
        file_name, *file_info = input().split()
        file_info[0] = tuple(map(int, file_info[0]))
        prm_dic[file_name] = file_info
    
    ans = []
    perm = {'R':6, 'W':2, 'X':1}
    for _ in range(int(input().strip())):
        name, file, oprt = input().split()
        if name == prm_dic[file][1]:
            ans.append('1' if perm[oprt] & prm_dic[file][0][0] else '0')
        elif name in grp_dic[prm_dic[file][2]]:
            ans.append('1' if perm[oprt] & prm_dic[file][0][1] else '0')
        else:
            ans.append('1' if perm[oprt] & prm_dic[file][0][2] else '0')

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