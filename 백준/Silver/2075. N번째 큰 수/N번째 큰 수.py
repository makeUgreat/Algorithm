import sys, heapq
# maxheap으로 채우면서 넣으면되겠다
n = int(input())

heap = []
for _ in range(n):
    row = map(int,sys.stdin.readline().split())
    for num in row:
        heapq.heappush(heap,num)

        # heap의 길이가 n을 넘으면
        # root를 지워서 작은 값들을 계속 빼준다
        # 이러면 메모리는 항상 n개만큼만 사용가능
        if len(heap) > n:
            heapq.heappop(heap)

print(heap[0])
