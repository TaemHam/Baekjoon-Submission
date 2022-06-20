# CP template Version 1.006
#import io
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
from heapq import heappush, heappop
#import bisect
#from bisect import insort_left as il
DEBUG = False

def main(f=None):
    init(f)
    # ######## INPUT AREA BEGIN ##########

    ### 입구(0)에서 정상(N-1)으로 가는 모든 최단경로를 찾아, 그에 포함된 모든 길의 길이의 합 * 2 를 출력하는 문제

    ### 최단 경로인 경우를 모두 heap에 넣어주면 시간초과가 나므로,
    #   다익스트라 후 역추적해 최단경로에 포함된 길을 찾을 수 있도록 하기 위해
    #   각 노드로 도착하는 최단경로일 때마다 새로운 배열의 다음 노드 번호(brd[nxt])에 길의 id와 현 노드 번호(pid, cur)를 저장해줌 

    ### 역추적은 평범한 BFS로 N-1부터 brd에 저장된 노드 번호를 따라가며 길의 id로 길이를 찾아 더해줌

    ### 마지막 정답 계산을 빠르게 하기 위해
    #   각 길의 길이 * 2를 저장해 놓은 배열(lng)를 만들고 인덱스 번호를 길의 id로 저장함 

    N, M = map(int, input().split())
    vis = [int(1e9)] * N
    vis[0] = 0
    grp = [[] for _ in range(N)]
    brd = [[] for _ in range(N)]
    que = [N-1]
    lng = []
    ans = 0
    heap = [(0, 0, [])]

    for m in range(M):
        u, v, d = map(int, input().split())
        lng.append(2*d)
        grp[u].append((v, d, m))
        grp[v].append((u, d, m))
    
    while heap:
        cds, cur = heappop(heap)
        if cds > vis[cur]:
            continue

        for nxt, tds, pid in grp[cur]:
            nds = cds + tds
            if nds < vis[nxt]:
                brd[nxt] = [(pid, cur)]
                vis[nxt] = nds
                heappush(heap, (nds, nxt))
            elif nds == vis[nxt]:
                brd[nxt].append((pid, cur))
    
    for cur in que:
        for pid, nxt in brd[cur]:
            ans += lng[pid]
            if vis[nxt]:
                vis[nxt] = 0
                que.append(nxt)
    
    return ans

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
    input = sys.stdin.readline #io.BytesIO(os.read(0, os.fstat(0).st_size)).readline 
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