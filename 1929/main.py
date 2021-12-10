a,b = list(map(int,input().split()))
c = int(b**(0.5))
arr = [1,1] + [0 for _ in range(b-1)]
for i in range (2,c+1):
    j=2
    while i*j <= b:
        arr[i*j] = 1
        j += 1
for i in range (a,b+1):
    if arr[i] == 0: print (i)