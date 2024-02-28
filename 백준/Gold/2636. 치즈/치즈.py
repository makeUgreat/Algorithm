import sys
from collections import deque

n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]

diy = [-1,1,0,0]
dix = [0,0,-1,1]


# 치즈가 다 녹을 때 까지


def melt_chz(sy,sx):
    # 공기랑 닿은 치즈를 모두 'c'로 바꿔 녹일 준비를 한다
    visited = [[False] * m for _ in range(n)]
    q=deque()
    q.append([sy,sx])
    visited[sy][sx] =True

    while q:
        y,x = q.popleft()
        for i in range(4):
            dy = y+diy[i]
            dx = x+dix[i]
            if dy<0 or dx<0 or dy>=n or dx>=m: continue
            if grid[dy][dx] == 1:
                grid[dy][dx] = 'c'

            if grid[dy][dx] == 0:
                if not visited[dy][dx]:
                    visited[dy][dx] = True
                    q.append([dy,dx])

time = 0
while True:
    time += 1
    melt_chz(0,0)
    # print(time)
    # for g in grid:
    #     print(*g)
    # print('-----------')

    chz_cnt = 0
    end_flag = True
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                end_flag = False
            if grid[i][j] == 'c':
                chz_cnt += 1
                grid[i][j] = 0


    if end_flag:
        print(time)
        print(chz_cnt)
        break



