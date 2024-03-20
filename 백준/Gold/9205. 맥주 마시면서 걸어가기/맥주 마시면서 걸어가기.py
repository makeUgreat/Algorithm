from collections import deque

diy = [-1,1,0,0]
dix = [0,0,-1,1]
def bfs(sy,sx):
    q = deque()
    q.append([sy,sx,20])
    visit = set()

    while q:
        y,x,beer = q.popleft()
        if abs(ey - y) + abs(ex-x) <= beer * 50:
            return "happy"


        for ny,nx in conv:
            if (ny,nx) not in visit and (abs(ny-y) + abs(nx-x)) <= beer * 50:
                visit.add((ny,nx))
                q.append([ny,nx,20])

    return "sad"


t = int(input())

for _ in range(t):
    conv = deque()
    n = int(input()) # 편의점 갯수
    sx,sy = map(int,input().split()) # 상근이네 좌표
    for _ in range(n):
        x,y = map(int,input().split())
        conv.append([y,x])
    ex,ey = map(int,input().split()) # 락페 좌표

    print(bfs(sy,sx))

