import sys
from collections import deque

n,m = map(int,input().split())
grid = [list(input()) for _ in range(n)]

diy=[-1,1,0,0]
dix=[0,0,-1,1]


def escape():
    visit = [[False] * m for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'J':
                q.append(['J',i,j,1])
                visit[i][j] = True
                # 지훈이가 가장자리에 있는 경우 바로 탈출
                if i == 0 or j == 0 or i == (n - 1) or j == (m - 1):
                    return 1
            if grid[i][j] == 'F':
                # 불부터 퍼지게
                q.appendleft(['F',i,j,1])

    while q:
        Type,y,x,time = q.popleft()
        # 
        # print(Type, time)
        # for g in grid:
        #     print(*g)
        # print('------------')

        if Type == 'J':
            for i in range(4):
                dy = y+diy[i]
                dx = x+dix[i]

                if dy<0 or dx<0 or dy>=n or dx>=m: continue
                if grid[dy][dx] == '.':
                    if visit[dy][dx]: continue
                    visit[dy][dx] = True
                    grid[dy][dx] = 'J'
                    q.append(['J',dy,dx,time+1])

                    if dy == 0 or dx == 0 or dy == (n-1) or dx == (m-1):
                        return time + 1

        else:
            for i in range(4):
                dy = y+diy[i]
                dx = x+dix[i]
                if dy<0 or dx<0 or dy>=n or dx>=m: continue
                if grid[dy][dx] == '.' or grid[dy][dx] == 'J':
                    grid[dy][dx] = 'F'
                    q.append(['F',dy,dx,time+1])


    return "IMPOSSIBLE"




print(escape())

