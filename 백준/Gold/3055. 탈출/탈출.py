import sys
from collections import deque

n,m = map(int,input().split())
grid = [list(input()) for _ in range(n)]
h_visit = [[False] * m for _ in range(n)]

diy = [0,0,-1,1]
dix = [-1,1,0,0]
def bfs():
    q = deque()

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                q.appendleft([i,j,0,'water']) # 물인 경우 큐에 넣되 먼저 퍼지게 맨 앞에 넣는다
            if grid[i][j] == 'D':
                fy,fx = i,j # 목적지
            if grid[i][j] == 'S':
                q.append([i,j,0,'hog']) # 고슴도치 시작위치
                h_visit[i][j] = True

    while q:
        y,x,time,char = q.popleft()


        # print(y,x,time,char)

        for i in range(4):
            dy = y + diy[i]
            dx = x + dix[i]

            if dy<0 or dx<0 or dy>=n or dx>=m: continue
            # 물이나 고슴도치나 돌로는 이동할 수 없다
            if grid[dy][dx] == 'X': continue

            if char == 'water': # 큐가 물인경우
                if grid[dy][dx] == 'D' or grid[dy][dx] == '*': continue # 비버의 굴로는 퍼질 수 없다
                grid[dy][dx] = '*'
                q.append([dy,dx,time+1,'water'])
                # for g in grid:
                #     print(*g)
                # print('-----', time)


            elif char == 'hog' and not h_visit[dy][dx]: # 큐가 고슴도치인 경우
                if grid[dy][dx] == '*': continue # 물로는 이동할 수 없다
                if dy == fy and dx == fx: # 비버굴에 도착하면 종료
                    return time+1

                q.append([dy,dx,time+1,'hog'])
                h_visit[dy][dx] =True

    return 'KAKTUS'

print(bfs())