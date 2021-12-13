import sys
n,m = map(int,input().split())
mat = []
for _ in range(n):
    mat.append(list(sys.stdin.readline().strip()))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
q = [[0,0]]
mat[0][0] = 1

while q:
    x,y = q[0][0], q[0][1]
    del q[0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and mat[nx][ny] == '1':
            q.append((nx,ny))
            mat[nx][ny] = mat[x][y] + 1

print(mat[-1][-1])








#------- 내가 푼 방법 --------
####n,m = map(int,input().split())
####mat = [sys.stdin.readline().strip() for _ in range(n)]
####dx = [1,-1,0,0]
####dy = [0,0,1,-1]
####grp = dict()
####q = deque([(0,0)])
####for x in range(n):
    ####for y in range(m):
        ####if mat[x][y] != '0':
            ####pos = []
            ####for i in range(4):
                ####nx = x + dx[i]
                ####ny = y + dy[i]
                ####if 0<=nx<n and 0<=ny<m and mat[nx][ny] != '0':
                    ####pos.append((nx,ny))
            ####grp[(x,y)] = pos
####mov = 1
####brdth = len(q)
####vst = set()
####while q:
    ####c = q.popleft()
    ####if c == (n-1,m-1):
        ####break
    ####vst.add(c)
    ####for i in grp[c]:
        ####if i not in vst:
            ####q.append(i)
    ####brdth -= 1
    ####if brdth == 0:
        ####mov += 1
        ####brdth = len(q)
####print(mov)
    
