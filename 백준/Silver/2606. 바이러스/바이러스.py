from collections import deque

n = int(input())
tree = [ [] for _ in range(n+1)]

e = int(input())
for _ in range(e):
    v,w = map(int,input().split())
    tree[v].append(w)
    tree[w].append(v)

visit = [False] * (n+1)

def bfs(start):
    q = deque()
    q.append(start)
    visit[start] = True
    ans = 0
    while q:
        now = q.popleft()
        for next in tree[now]:
            if not visit[next]:
                visit[next] = True
                q.append(next)
                ans += 1

    return ans

print(bfs(1))
