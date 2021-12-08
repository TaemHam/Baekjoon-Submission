import sys
n = int(input())
case = [list(map(int,input().split())) for _ in range(n)]
for i in case:
    h, w, c = i
    print((((c-1)%h+1)*100) + ((c-1)//h+1))