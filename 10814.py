import sys
n = int(input())
arr = [list(sys.stdin.readline().split()) for _ in range(n)]
for i in arr: i[0]=int(i[0])
arr.sort(key=lambda x:x[0])
for i in arr: 
    i[0]=str(i[0])
    i=' '.join(i)
    print(i)