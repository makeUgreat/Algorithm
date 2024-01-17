from collections import deque

n,m = map(int,input().split())
grid = [ list(map(int,input().split())) for _ in range(n)]

diy = [-1,0,1,0]
dix = [0,-1,0,1]

def count_around_sea(y,x):
    cnt = 0
    for i in range(4):
        dy = y + diy[i]
        dx = x + dix[i]
        if dy<0 or dx<0 or dy>=n or dx>=m: continue
        if grid[dy][dx] == 0:
            cnt += 1

    return cnt

def bfs(sy,sx):
    q = deque()
    q.append([sy,sx])
    visit[sy][sx] = True

    while q:
        y,x = q.popleft()
        adjCnt = 0
        adjCnt = count_around_sea(y,x)
        melting_grid[y][x] = max(0,grid[y][x] - adjCnt)


        for i in range(4):
            dy = y + diy[i]
            dx = x + dix[i]

            if dy<0 or dx<0 or dy>=n or dx>=m: continue
            if not visit[dy][dx]:
                if grid[dy][dx] >= 1:
                    q.append([dy,dx])
                    visit[dy][dx] = True



years = 0
while 1:
    visit = [[False] * m for _ in range(n)]
    melting_grid = [[0]*m for _ in range(n)]
    iceberg = 0

    for i in range(n):
        for j in range(m):
            if visit[i][j]: continue
            if grid[i][j] >= 1:
                bfs(i,j)
                iceberg += 1

    if iceberg >= 2:
        break

    all_melted = True
    for i in range(n):
        for j in range(m):
            if grid[i][j] >= 1:
                all_melted = False
                grid[i][j] = melting_grid[i][j]

    if all_melted:
        years = 0
        break

    years += 1
    # for g in grid:
    #     print(*g)
    # print('------------')

print(years)
