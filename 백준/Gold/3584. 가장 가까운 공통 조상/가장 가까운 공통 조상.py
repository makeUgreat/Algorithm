import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

# 예를 들어 15와 11의 공통 조상을 찾는다고하면
# 각각 15와 11로부터 출발해서 루트로 탐색을 하면서 층마다 기록함
# 기록을 앞에서부터 비교하면서 가장 처음 발견된 공통 조상이 두 노드의 가장 가까운 공통조상

T = int(input())
for tc in range(T):
    N = int(input())
    tree = [ [] for _ in range(N+1) ]
    for _ in range(N-1):
        a,b = map(int,input().split())
        # a가 b의 부모이지만
        # 자식에서 출발해서 부모로 가야하므로 트리를 반대로 저장
        tree[b].append(a)

    node1, node2 = map(int,input().split())
    ancestor = [0] * (N+1)
    anc_depth = [0] * (N+1)

    def dfs(now,depth):
        ancestor[now] += 1
        anc_depth[now] = depth
        for next in tree[now]:
            dfs(next,depth+1)

    dfs(node1,0)
    dfs(node2,0)

    same_anc = []
    for i in range(len(ancestor)):
        if ancestor[i] >= 2:
            same_anc.append(i)

    min_v = sys.maxsize
    answer_node = 0
    for node in same_anc:
        if anc_depth[node] < min_v:
            min_v = anc_depth[node]
            answer_node = node

    print(answer_node)