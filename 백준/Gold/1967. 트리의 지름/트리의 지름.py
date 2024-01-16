import sys
sys.setrecursionlimit(10000)

n = int(input())
graph = [[] for _ in range(n+1) ]
for _ in range(n-1):
    u,v,cost = map(int,input().split())
    graph[u].append([v,cost])
    graph[v].append([u,cost])



def dfs(now,dist):
    global max_distance, max_node
    visit[now] = True

    if dist > max_distance:
        max_node = now
        max_distance = dist

    for next_node, next_dist in graph[now]:
        if not visit[next_node]:
            dfs(next_node, dist+next_dist)

max_node = 0

max_distance = -21e8
distances = [0] * (n+1)
visit = [False] * (n+1)
dfs(1,0)

max_distance = -21e8
visit = [False] * (n+1)
dfs(max_node,0)

print(max_distance)



