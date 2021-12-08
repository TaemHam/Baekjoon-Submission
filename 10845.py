from sys import stdin
n = int(input())
cmd = [stdin.readline().strip() for _ in range(n)]
que,a,b = {},0,1
for i in cmd:
    if 'push' in i:
        a += 1
        que[a] = int(i[5:])
    elif 'pop' in i:
        try:
            print(que[b])
            del que[b]
            b += 1
        except:
            print(-1)
    elif 'size' in i: print(len(que))
    elif 'empty' in i: print(1 if len(que) == 0 else 0)
    elif 'front' in i: 
        try: print(que[b])
        except: print(-1)
    else:
        try: print(que[a])
        except: print(-1)