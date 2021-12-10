import sys
n = int(input())
arr = set([sys.stdin.readline().strip() for _ in range(n)])
ans = sorted(sorted(arr),key=len)
for i in ans: print(i)