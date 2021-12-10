n = int(input())
na = list(map(int,input().split()))
m = int(input())
ma = list(map(int,input().split()))
d = dict()
for i in na: d[i] = True
for j in ma: 
    if j in d: print(1)
    else: print(0)
