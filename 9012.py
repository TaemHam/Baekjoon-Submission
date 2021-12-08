import sys
n = int(input())
s = [sys.stdin.readline().strip() for i in range(n)]
for i in s:
    cnt = 0
    for j in i:
        if j == '(': cnt += 1
        elif j == ')': cnt -= 1
        if cnt <= -1:
            break
    if cnt == 0: print('YES')
    else: print('NO')