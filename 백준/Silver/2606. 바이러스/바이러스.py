import sys
from collections import deque

n = int(input())
k = int(input())

graph = [ [] for _ in range(n+1) ]
for _ in range(k):
    v,w = map(int,input().split())
    graph[v].append(w)
    graph[w].append(v)


def bfs(start):
    cnt = 0

    visit = [False] * (n+1)
    q = deque()
    q.append(start)

    visit[start] = True

    while q:
        now = q.popleft()

        for next in graph[now]:
            if not visit[next]:
                visit[next] = True
                cnt += 1

                q.append(next)
                
    return cnt

print(bfs(1))



