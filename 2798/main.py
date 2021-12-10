a, b = list(map(int,input().split()))
arr = list(map(int,input().split()))
ans = 0
for i in range(a):
    for j in range(i+1,a):
        for k in range(j+1,a):
            s = arr[i]+arr[j]+arr[k]
            if s>ans and s<=b: ans = s
print(ans)