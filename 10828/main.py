n = int(input())
cmd = [input() for _ in range(n)]
arr = []
for i in cmd:
    if 'push' in i:
        arr.append(int(i[5:]))
    elif 'pop' in i:
        try:
            a = arr.pop()
            print(a)
        except: print(-1)
    elif 'size' in i: print(len(arr))
    elif 'empty' in i: 
        print(1 if len(arr)==0 else 0)
    else: 
        try:
            print(arr[-1])
        except:
            print(-1)