import sys
from collections import deque

diy = [-1,1,0,0]
dix = [0,0,-1,1]
def escape(arr,n,m):
    visit = [[False] * m for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '@':
                q.append(['I',i,j,1])
                visit[i][j] = True

                if i==0 or j==0 or i==(n-1) or j==(m-1):
                    return 1

            if arr[i][j] == '*':
                q.appendleft(['F',i,j,1])


    while q:
        Type,y,x,time = q.popleft()

        # print(time)
        # for g in grid:
        #     print(*g)
        # print('------------')

        for i in range(4):
            dy = y+diy[i]
            dx = x+dix[i]

            if dy<0 or dx<0 or dy>=n or dx>=m: continue
            if Type == 'I':
                if arr[dy][dx] == '.':
                    if not visit[dy][dx]:
                        visit[dy][dx]= True
                        q.append(['I',dy,dx,time+1])

                        if dy==0 or dx==0 or dy==(n-1) or dx==(m-1):
                            return time +1

            else:
                if arr[dy][dx] == '.' or arr[dy][dx] == '@':
                    q.append(['F', dy, dx, time + 1])
                    arr[dy][dx] = 'F'

    return 'IMPOSSIBLE'



t = int(input())
for tc in range(t):
    m,n = map(int,input().split())
    grid = [ list(input()) for _ in range(n) ]
    print(escape(grid,n,m))


