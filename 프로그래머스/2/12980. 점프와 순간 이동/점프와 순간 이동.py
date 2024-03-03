def solution(n):
    cost = 0
    while n >= 1:
    
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            cost += 1
        
    return cost