import sys
from collections import deque

m,n,h = map(int,input().split())
grid = []
for _ in range(h):
    grid.append([list(map(int,input().split())) for _ in range(n)])


diz = [0,0,0,0,-1,1]
diy = [-1,1,0,0,0,0]
dix = [0,0,-1,1,0,0]
def bfs():
    ifNotStart = True
    q = deque()
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if grid[k][i][j] == 1:
                    q.append([k,i,j,0])
                    ifNotStart = False

    if ifNotStart:
        return 0

    while q:
        z,y,x,time = q.popleft()

        for i in range(6):
            dz = z + diz[i]
            dy = y + diy[i]
            dx = x + dix[i]

            if dz < 0 or dz >= h: continue # z축 경계조건
            if dy < 0 or dx < 0 or dy >= n or dx >= m: continue # y,x 축 경계조건

            if grid[dz][dy][dx] == 0:
                q.append([dz,dy,dx,time+1])
                grid[dz][dy][dx] = time + 1


    return time


ans = bfs()

for k in range(h):
    for i in range(n):
        for j in range(m):
            if grid[k][i][j] == 0:
                ans = -1
print(ans)

