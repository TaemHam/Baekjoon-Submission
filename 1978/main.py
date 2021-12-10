import math
a,b = [list(map(int,input().split())) for _ in range(2)]
c = max(b)
d = int(math.sqrt(c))
l = [0 for _ in range(c+1)]
l[0], l[1] = 1, 1
for i in range(2,d+1):
    if l[i] == 0:
        j = 2
        while i*j <= c:
            l[i*j] = 1
            j += 1
cnt = 0
for k in b:
    if l[k] == 0 : cnt += 1
print(cnt)