n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

diy = [0,-1,1,0,0]
dix = [0,0,0,-1,1]

visit = [[False]*n for _ in range(n)]
def check(y,x):
    for i in range(5):
        dy = y + diy[i]
        dx = x + dix[i]

        if visit[dy][dx]:
            return 0

    return 1

def dfs(cnt):
    global total,min_v

    if total > min_v:
        return

    if cnt == 3:
        min_v = min(min_v,total)
        return

    for i in range(1,n-1):
        for j in range(1,n-1):
            if check(i,j):
                for k in range(5):
                    dy = i + diy[k]
                    dx = j + dix[k]
                    if dy<0 or dx<0 or dy>=n or dx>=n: continue
                    visit[dy][dx] = True
                    total += arr[dy][dx]

                dfs(cnt+1)

                for k in range(5):
                    dy = i + diy[k]
                    dx = j + dix[k]
                    if dy < 0 or dx < 0 or dy >= n or dx >= n: continue
                    visit[dy][dx] = False
                    total -= arr[dy][dx]


total = 0
min_v = 21e8
dfs(0)
print(min_v)