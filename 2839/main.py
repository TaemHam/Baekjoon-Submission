a = int(input())
b = a//5
for i in range(b,-1,-1):
    q, r = divmod((a-(5*i)),3)
    if r == 0: 
        print(i+q)
        break
else: print(-1)