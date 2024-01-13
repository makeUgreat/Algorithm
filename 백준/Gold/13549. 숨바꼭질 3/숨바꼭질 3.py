from collections import deque
import sys
n,k = map(int,input().split())

def bfs(start,destination):
    times = [sys.maxsize] * 100001
    q = deque()
    q.append([start,0])
    times[start] = 0

    while q:
        now,time = q.popleft()

        if now == destination:
            return time

        # 순간이동 하는 경우
        next = now*2
        if 0 <= next <= 100000:
            if time < times[next]:
                times[next] = time
                q.append([next,time])

        # 걷는 경우
        for next in (now-1,now+1):
            if 0 <= next <= 100000:
                if time+1 < times[next]:
                    times[next] = time+1
                    q.append([next,time+1])


ans = bfs(n,k)
print(ans)

