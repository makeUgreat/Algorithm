def solution(B, Y):
    total_tiles = B+Y
    cases = []

    # 타일 총 갯수 가능한 가로*세로 경우의 수 찾기
    for i in range(1, int(total_tiles**0.5)+1):
        if total_tiles % i == 0:
            cases.append([i,total_tiles//i])

    ans = []
    for hei,wid in cases: # 항상 가로>=세로 이므로 더 큰 값을 세로로(제곱근까지만 뽑았으니까)
        # 세로가 노란색 격자의 약수인 경우만
        # 갈색 격자가 항상 테두리를 둘러 쌓고 있으므로 노란색 격자가 위치할 수 있는 부분은 wid-2,hei-2 가 된다
        # 이 두 값이 주어지는 노란색 격자 전체 갯수와 같은 경우가 만족하는 경우의 수
        if (hei-2) * (wid-2) == Y:
            ans = [wid,hei]
    
    
    return ans