# CP template Version 1.006
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
#from itertools import product
#import collections
#from collections import deque
#from collections import defaultdict as dd
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
    
    h = int(input().strip())
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

                
    for _ in range(h):
        n, m = map(int, input().split())
        door = [[] for _ in range(26)]
        vis = [[0] * (m) for _ in range(n)]
        grp = []
        key = set()
        q = []
        ans = 0
        
        for y in range(n):
            t = list(input().strip())
            if y in [0, n-1]:
                step = 1
            else:
                step = m-1
            for x in range(0, m, step):

                if t[x] == '*':
                    continue
                
                elif t[x] == '.':
                    vis[y][x] = 1
                    q.append((y, x))
                    
                elif t[x] == '$':
                    ans += 1
                    vis[y][x] = 1
                    q.append((y, x))

                elif t[x].islower():
                    key.add(t[x])
                    vis[y][x] = 1
                    q.append((y, x))

                else:
                    door[ord(t[x].lower()) - 97].append((y, x))

            grp.append(t)

        key = key.union(set(list(input().strip())))
        if '0' in key:
            key.remove('0')

        for i in key:
            k = ord(i) - 97
            while door[k]:
                cy, cx = door[k].pop()
                vis[cy][cx] = 1
                q.append((cy, cx))

        while q:
            while q:
                y, x = q.pop()
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if 0 <= nx < m and 0 <= ny < n and vis[ny][nx] == 0 and grp[ny][nx] != '*':

                        if grp[ny][nx] == '.':
                            vis[ny][nx] = 1
                            q.append((ny, nx))

                        elif grp[ny][nx] == '$':
                            ans += 1
                            vis[ny][nx] = 1
                            q.append((ny, nx))

                        elif grp[ny][nx].islower():
                            key.add(grp[ny][nx])
                            vis[ny][nx] = 1
                            q.append((ny, nx))

                        else:
                            door[ord(grp[ny][nx].lower()) - 97].append((ny, nx))

            for i in key:
                k = ord(i) - 97
                while door[k]:
                    cy, cx = door[k].pop()
                    vis[cy][cx] = 1
                    q.append((cy, cx))

        print(ans)

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