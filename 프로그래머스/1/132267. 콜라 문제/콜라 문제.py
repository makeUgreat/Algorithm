def solution(a, b, n):
    answer = 0
    
    while n >= a:
        # 현재 보유한 빈병으로 받을 수 있는 새 콜라 계산
        new_coke = (n//a) * b
        answer += new_coke
        n = n%a + new_coke     
            
    return answer