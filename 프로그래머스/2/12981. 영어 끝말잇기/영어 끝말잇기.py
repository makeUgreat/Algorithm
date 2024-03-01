def solution(n, words):
    answer = [0,0]
    
    # 사용한 단어 저장해두기
    used = dict()
    # 첫 단어 항상 저장
    used[words[0]] = 1
    
    for i in range(1,len(words)):
        prev = words[i-1]
        now = words[i]
        
        # 이전 단어랑 이어지지 않거나
        # 이미 사용된 적 있는 경우
        if prev[-1] != now[0] or now in used:
            answer[0] = i%n + 1
            answer[1] = i//n + 1
            return answer
        
        
        # 지금까지는 이상 없었음
        # 해당 차례에 나온 문자저장
        used[now] = 1
    
            
    
    # 문제가 없었다면 그대로 0,0 출력
    return answer 
        
        
    
