def solution(arr):
    def calc(n,m):
        a = n
        b = m
        rest = 0
        while m:
            rest = n%m  # 나머지 저장
            n = m 
            m = rest
        
        return a*b//n
    
    LCM = calc(arr[0],arr[1])
    
    for i in range(2,len(arr)):
        temp = calc(LCM, arr[i])
        LCM = temp

    
    return LCM