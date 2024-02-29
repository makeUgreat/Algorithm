import sys
from collections import deque

n,k = map(int,input().split())
maps = [-1] * 100001
def bfs(n,k):
    maps[n] = n
    q = deque()
    q.append([n,0])

    while q:
        now, time = q.popleft()

        if now == k:
            return time

        for next in [now-1, now+1, now*2]:
            if 0 <= next <= 100000 and maps[next] == -1:
                maps[next] = now
                q.append([next, time+1])


if n==k:
    print(0)
    print(n)
else:
    time = bfs(n, k)
    print(time)

    path = [k]
    while path[-1] != n:  # 시작 위치에 도달할 때까지 역추적
        path.append(maps[path[-1]])
    path.reverse()  # 올바른 순서로 뒤집기

    print(*path)  # 최단 경로 출력