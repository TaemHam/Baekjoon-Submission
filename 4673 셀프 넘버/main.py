p = 1
grp = [0] * 10001
ans = []
while p <= 9993:
    if grp[p] == 1:
        p += 1
        continue
    ans.append(p)
    t = p + sum(map(int, list(str(p))))
    while t <= 9993:
        if grp[t]:
            break
        grp[t] = 1
        t = t + sum(map(int, list(str(t))))
    p += 1

for i in ans:
    print(i)