from sys import stdin
n = int(input())
m = [list(map(int,stdin.readline().split())) for _ in range(n)]
m.sort(key=lambda x:(x[0], x[1]))
for i in m: print(' '.join(str(j) for j in i))