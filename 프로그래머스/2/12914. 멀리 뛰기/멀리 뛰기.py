def solution(n):
    dp = [1,2]
    
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    for i in range(2,n):
        tmp = dp[i-2] + dp[i-1]
        dp.append(tmp)  
    
    answer = dp[n-1]
    
    
    return answer % 1234567