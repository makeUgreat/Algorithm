def solution(k, tangerine):
    # tangerine 에서 k개의 숫자를 뽑는데
    # 이 때 숫자의 종류가 최소인 경우
    # 숫자 종류의 갯수는 set으로 넣고 길이를 세면되는데
    # 종류가 최소이려면 같은 숫자의 갯수가 가장 많은 것 부터 넣으면 될듯
    # 숫자의 갯수는 어떻게 세지? -> 어떤게 효율적일까
    # 어차피 count 쓸거면 차라리 딕셔너리 만들어서 숫자별 갯수 저장하자
    
    bucket = dict()
    for t in tangerine:
        bucket[t] = bucket.get(t, 0) + 1

        
    sorted_bucket = sorted(bucket.items(), key=lambda item: item[1], reverse=True)
    
    answer = 0
    for tang_size, cnt in sorted_bucket:
        if k <= 0:
            break
        
        k -= cnt
        answer += 1
        

    return answer