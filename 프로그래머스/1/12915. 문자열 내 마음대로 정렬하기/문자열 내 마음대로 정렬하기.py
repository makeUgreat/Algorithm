def solution(strings, n):
    # n번째 문자와 문자열을 튜플로 저장
    tuple_lists = [ (s[n], s ) for s in strings ]
    
    # 튜플의 0번째 요소를 기준으로 정렬하되 리스트로 저장
    
    answer = [ s for _, s in sorted(tuple_lists) ]
    
    return answer