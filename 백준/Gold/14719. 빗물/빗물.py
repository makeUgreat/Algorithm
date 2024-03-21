h,w = map(int,input().split())
grid = [[0]*w for _ in range (h)]
blocks = list(map(int,input().split()))

# 블록 배치
for i, height in enumerate(blocks):
    for j in range(height):
        grid[h-j-1][i] = 1

# for g in grid:
#     print(*g)


water = 0
for i in range(h):
    left_block = False
    tmp = 0
    for j in range(w):
        if grid[i][j] == 1:
            if left_block:  # 왼쪽 블록이 존재할 때만 빗물 계산
                water += tmp
            tmp = 0  # 블록을 만나면 임시 빗물 저장소 초기화
            left_block = True  # 왼쪽 블록 존재 표시
        else:
            tmp += 1  # 블록 사이 공간에 빗물이 고임

print(water)